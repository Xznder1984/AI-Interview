/**
 * AI Mock Interview - Frontend JavaScript
 * Handles UI interactions and API communication with user-provided API keys
 */

class InterviewApp {
    constructor() {
        this.currentSessionId = null;
        this.currentPersona = null;
        this.interviewStartTime = null;
        this.timerInterval = null;
        this.isWaitingForResponse = false;
        this.apiKey = sessionStorage.getItem('openrouter_api_key');
        this.messages = [];
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        
        if (this.apiKey) {
            // User already logged in
            this.showSection('welcome-section');
            this.showApiStatus();
            this.loadPersonas();
        } else {
            // Show login form
            this.showSection('login-section');
            this.hideApiStatus();
        }
    }

    setupEventListeners() {
        // Login section
        document.getElementById('login-btn')?.addEventListener('click', () => this.handleLogin());
        document.getElementById('api-key-input')?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleLogin();
            }
        });

        // Logout button
        document.getElementById('logout-btn')?.addEventListener('click', () => this.handleLogout());

        // Welcome section
        document.getElementById('personas-container')?.addEventListener('click', (e) => {
            const card = e.target.closest('.persona-card');
            if (card) {
                this.startInterview(card.dataset.persona);
            }
        });

        // Interview section
        document.getElementById('send-response-btn')?.addEventListener('click', () => this.sendResponse());
        document.getElementById('response-input')?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendResponse();
            }
        });
        document.getElementById('end-interview-btn')?.addEventListener('click', () => this.endInterview());

        // Feedback section
        document.getElementById('new-interview-btn')?.addEventListener('click', () => this.resetToWelcome());
        document.getElementById('download-feedback-btn')?.addEventListener('click', () => this.downloadFeedback());
    }

    handleLogin() {
        const apiKeyInput = document.getElementById('api-key-input');
        const apiKey = apiKeyInput?.value?.trim();

        if (!apiKey) {
            this.showError('Please paste your OpenRouter API key');
            return;
        }

        if (!apiKey.startsWith('sk-or-v1-')) {
            this.showError('API key should start with "sk-or-v1-". Check OpenRouter.ai/keys');
            return;
        }

        // Store API key in sessionStorage (only in user's browser, never sent to backend)
        sessionStorage.setItem('openrouter_api_key', apiKey);
        this.apiKey = apiKey;

        // Clear input and proceed
        apiKeyInput.value = '';
        this.showSection('welcome-section');
        this.showApiStatus();
        this.loadPersonas();
    }

    handleLogout() {
        sessionStorage.removeItem('openrouter_api_key');
        this.apiKey = null;
        this.currentSessionId = null;
        this.messages = [];
        this.showSection('login-section');
        this.hideApiStatus();
        document.getElementById('api-key-input').value = '';
        document.getElementById('api-key-input').focus();
    }

    async loadPersonas() {
        try {
            this.showLoading('Loading interview types...');
            const response = await fetch('/api/personas');
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to load personas');
            }

            this.displayPersonas(data.personas);
            this.hideLoading();
        } catch (error) {
            this.showError('Failed to load interview types: ' + error.message);
            this.hideLoading();
        }
    }

    displayPersonas(personas) {
        const container = document.getElementById('personas-container');
        container.innerHTML = '';

        personas.forEach(persona => {
            const card = document.createElement('div');
            card.className = 'persona-card';
            card.dataset.persona = persona.id;
            card.innerHTML = `
                <div class="persona-card-content">
                    <h3>${persona.emoji} ${persona.name}</h3>
                    <p class="persona-title">${persona.title}</p>
                    <p class="persona-company">${persona.company}</p>
                    <p class="persona-description">${persona.description}</p>
                    <button class="btn btn-primary">Start Interview</button>
                </div>
            `;
            container.appendChild(card);
        });
    }

    async startInterview(personaId) {
        try {
            if (!this.apiKey) {
                this.showError('API key not found. Please log in again.');
                this.handleLogout();
                return;
            }

            this.showLoading('Starting interview...');

            const response = await fetch('/api/interview/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-API-Key': this.apiKey  // Send API key in header
                },
                body: JSON.stringify({ persona_id: personaId })
            });

            const data = await response.json();

            if (!response.ok) {
                if (response.status === 401) {
                    this.showError('Invalid API key. Please check and try again.');
                    this.handleLogout();
                } else {
                    throw new Error(data.error || 'Failed to start interview');
                }
                this.hideLoading();
                return;
            }

            this.currentSessionId = data.session_id;
            this.currentPersona = data.persona;
            this.interviewStartTime = Date.now();
            this.messages = [];

            // Display interviewer info
            document.getElementById('interviewer-name').textContent = data.persona.name;
            document.getElementById('interviewer-title').textContent = data.persona.title;
            document.getElementById('interviewer-company').textContent = data.persona.company;

            // Clear chat and display opening question
            const chatMessages = document.getElementById('chat-messages');
            chatMessages.innerHTML = '';

            const messageDiv = document.createElement('div');
            messageDiv.className = 'message interviewer-message';
            messageDiv.innerHTML = `
                <div class="message-content">
                    <p>${this.escapeHtml(data.opening_question)}</p>
                </div>
                <div class="message-time">${new Date().toLocaleTimeString()}</div>
            `;
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Store opening question
            this.messages.push({
                role: 'assistant',
                content: data.opening_question
            });

            this.showSection('interview-section');
            document.getElementById('response-input').focus();
            this.startTimer();
            this.hideLoading();
        } catch (error) {
            this.showError('Error starting interview: ' + error.message);
            this.hideLoading();
        }
    }

    async sendResponse() {
        const input = document.getElementById('response-input');
        const message = input.value.trim();

        if (!message || this.isWaitingForResponse) {
            return;
        }

        if (!this.apiKey) {
            this.showError('API key lost. Please log in again.');
            this.handleLogout();
            return;
        }

        // Add user message to chat
        const chatMessages = document.getElementById('chat-messages');
        const userMessageDiv = document.createElement('div');
        userMessageDiv.className = 'message user-message';
        userMessageDiv.innerHTML = `
            <div class="message-content">
                <p>${this.escapeHtml(message)}</p>
            </div>
            <div class="message-time">${new Date().toLocaleTimeString()}</div>
        `;
        chatMessages.appendChild(userMessageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        // Store message
        this.messages.push({
            role: 'user',
            content: message
        });

        input.value = '';
        this.isWaitingForResponse = true;
        document.getElementById('send-response-btn').disabled = true;

        try {
            this.showLoading('Interviewer is thinking...');

            const response = await fetch('/api/interview/respond', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-API-Key': this.apiKey  // Send API key in header
                },
                body: JSON.stringify({
                    session_id: this.currentSessionId,
                    user_message: message
                })
            });

            const data = await response.json();

            if (!response.ok) {
                if (response.status === 401) {
                    this.showError('Invalid API key. Please check and try again.');
                    this.handleLogout();
                } else {
                    throw new Error(data.error || 'Failed to get AI response');
                }
                this.hideLoading();
                this.isWaitingForResponse = false;
                document.getElementById('send-response-btn').disabled = false;
                return;
            }

            // Add AI response to chat
            const aiMessageDiv = document.createElement('div');
            aiMessageDiv.className = 'message interviewer-message';
            aiMessageDiv.innerHTML = `
                <div class="message-content">
                    <p>${this.escapeHtml(data.response)}</p>
                </div>
                <div class="message-time">${new Date().toLocaleTimeString()}</div>
            `;
            chatMessages.appendChild(aiMessageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;

            // Store response
            this.messages.push({
                role: 'assistant',
                content: data.response
            });

            this.hideLoading();
        } catch (error) {
            this.showError('Error: ' + error.message);
            this.hideLoading();
        } finally {
            this.isWaitingForResponse = false;
            document.getElementById('send-response-btn').disabled = false;
            document.getElementById('response-input').focus();
        }
    }

    startTimer() {
        let seconds = 0;
        this.timerInterval = setInterval(() => {
            seconds++;
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            document.getElementById('timer').textContent = 
                `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
        }, 1000);
    }

    async endInterview() {
        if (!this.currentSessionId) {
            return;
        }

        clearInterval(this.timerInterval);

        try {
            this.showLoading('Generating your feedback...');

            const response = await fetch('/api/interview/end', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-API-Key': this.apiKey  // Send API key in header
                },
                body: JSON.stringify({ session_id: this.currentSessionId })
            });

            const data = await response.json();

            if (!response.ok) {
                if (response.status === 401) {
                    this.showError('Invalid API key. Please check and try again.');
                    this.handleLogout();
                } else {
                    throw new Error(data.error || 'Failed to end interview');
                }
                this.hideLoading();
                return;
            }

            // Display feedback
            document.getElementById('feedback-duration').textContent = data.duration;
            document.getElementById('feedback-message-count').textContent = data.message_count;
            document.getElementById('feedback-display').innerHTML = 
                `<p>${this.escapeHtml(data.feedback)}</p>`;

            // Display transcript
            let transcriptHtml = '';
            this.messages.forEach((msg, index) => {
                const role = msg.role === 'user' ? 'You' : this.currentPersona.name;
                const className = msg.role === 'user' ? 'user' : 'interviewer';
                transcriptHtml += `
                    <div class="transcript-entry ${className}">
                        <strong>${role}:</strong>
                        <p>${this.escapeHtml(msg.content)}</p>
                    </div>
                `;
            });
            document.getElementById('transcript-display').innerHTML = transcriptHtml;

            this.showSection('feedback-section');
            this.hideLoading();
        } catch (error) {
            this.showError('Error ending interview: ' + error.message);
            this.hideLoading();
        }
    }

    resetToWelcome() {
        this.currentSessionId = null;
        this.currentPersona = null;
        this.messages = [];
        clearInterval(this.timerInterval);
        document.getElementById('timer').textContent = '00:00';
        this.showSection('welcome-section');
    }

    downloadFeedback() {
        const duration = document.getElementById('feedback-duration').textContent;
        const feedback = document.getElementById('feedback-display').innerText;
        const transcript = document.getElementById('transcript-display').innerText;

        const content = `
AI MOCK INTERVIEW FEEDBACK
==========================

Interviewer: ${this.currentPersona.name}
Duration: ${duration}

FEEDBACK
--------
${feedback}

TRANSCRIPT
----------
${transcript}

Generated on: ${new Date().toLocaleString()}
        `;

        const blob = new Blob([content], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `interview-feedback-${Date.now()}.txt`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    }

    showSection(sectionId) {
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });
        const section = document.getElementById(sectionId);
        if (section) {
            section.classList.add('active');
        }
    }

    showLoading(text = 'Loading...') {
        document.getElementById('loading-modal').style.display = 'flex';
        document.getElementById('loading-text').textContent = text;
    }

    hideLoading() {
        document.getElementById('loading-modal').style.display = 'none';
    }

    showError(message) {
        alert('Error: ' + message);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    showApiStatus() {
        const status = document.getElementById('api-status');
        if (status) {
            status.style.display = 'flex';
        }
    }

    hideApiStatus() {
        const status = document.getElementById('api-status');
        if (status) {
            status.style.display = 'none';
        }
    }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new InterviewApp();
});

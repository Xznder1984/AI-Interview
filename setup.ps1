# AI Mock Interview - PowerShell Setup Script
# This script sets up the application on Windows with PowerShell

Write-Host ""
Write-Host "====================================" -ForegroundColor Cyan
Write-Host " AI Mock Interview - Setup" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python is installed: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "[ERROR] Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Check if pip is installed
try {
    pip --version > $null 2>&1
    Write-Host "[OK] pip is installed" -ForegroundColor Green
}
catch {
    Write-Host "[ERROR] pip is not installed" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Create virtual environment
Write-Host "[SETUP] Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to create virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Virtual environment created" -ForegroundColor Green
Write-Host ""

# Activate virtual environment
Write-Host "[SETUP] Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to activate virtual environment" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Virtual environment activated" -ForegroundColor Green
Write-Host ""

# Install requirements
Write-Host "[SETUP] Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Dependencies installed" -ForegroundColor Green
Write-Host ""

# Check for .env file
if (-not (Test-Path ".env")) {
    Write-Host "[SETUP] Creating .env file from .env.example..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "[WARNING] Please edit .env and add your OPENAI_API_KEY" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Open .env with a text editor and replace:" -ForegroundColor Yellow
    Write-Host "  OPENAI_API_KEY=your_openai_api_key_here" -ForegroundColor Yellow
    Write-Host "with your actual API key from https://platform.openai.com/api-keys" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to continue"
}
else {
    Write-Host "[OK] .env file already exists" -ForegroundColor Green
    Write-Host ""
}

# Final message
Write-Host "====================================" -ForegroundColor Cyan
Write-Host " Setup Complete!" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application, run:" -ForegroundColor White
Write-Host "  python src/main.py" -ForegroundColor Green
Write-Host ""
Write-Host "The application will be available at:" -ForegroundColor White
Write-Host "  http://localhost:5000" -ForegroundColor Green
Write-Host ""
Read-Host "Press Enter to exit"

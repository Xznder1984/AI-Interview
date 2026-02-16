# AI Interview — Local Mock Interview App

AI Interview is a small Flask + vanilla JS application that lets users run mock interviews powered by OpenRouter. Users supply their own OpenRouter API key in the browser — the server does not store it.

Features

- Multiple interview personas
- User-provided OpenRouter API key (stored in browser session only)
- Simple web UI for asking/answering questions and exporting feedback

Quick links

- Quickstart: `QUICKSTART.md`
- API Key guide: `API_KEY_GUIDE.md`
- Deployment notes: `DEPLOYMENT.md`

Running locally

1. Create a Python 3.8+ virtual environment and install dependencies.

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

2. Run the app:

    python src/main.py

3. Open the app in your browser: <http://localhost:5000> and paste your OpenRouter API key when prompted.

Contributing

- Keep user secrets out of the repository.
- Double-check that no local file paths, machine names, or API keys exist in the docs.

License

MIT
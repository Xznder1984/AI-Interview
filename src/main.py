"""
Main entry point for AI Mock Interview App
Handles startup and configuration
Users provide their own OpenRouter API key via the web interface
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for Flask secret key (optional, generate one if needed)
if not os.getenv("FLASK_SECRET_KEY"):
    print("⚠️  Note: FLASK_SECRET_KEY not set in .env. Using default.")
    print("    For production, set a proper secret key.\n")

# Import and run Flask app
from app import app

if __name__ == "__main__":
    print("🚀 Starting AI Mock Interview Application...")
    print("📍 Server running at http://localhost:5000")
    print("\n📝 Available Interview Personas:")
    print("  • MIT Admissions Officer - Advanced college admission interview")
    print("  • Finance Broker - Advanced investment banking interview")
    print("  • Tech CTO - Advanced technical interview")
    print("  • HR Manager - Intermediate behavioral interview")
    print("  • Management Consultant - Advanced case interview")
    print("\n🔑 Users will provide their own OpenRouter API key via the web form")
    print("   Get free API keys at: https://openrouter.ai")
    print("\n💡 Press CTRL+C to stop the server\n")
    
    app.run(debug=True, host="0.0.0.0", port=5000)

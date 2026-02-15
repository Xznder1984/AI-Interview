@echo off
REM AI Mock Interview - Windows Setup Script
REM This script sets up the application on Windows

echo.
echo ====================================
echo  AI Mock Interview - Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
echo.

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not installed
    pause
    exit /b 1
)

echo [OK] pip is installed
echo.

REM Create virtual environment
echo [SETUP] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo [SETUP] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment activated
echo.

REM Install requirements
echo [SETUP] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.

REM Check for .env file
if not exist .env (
    echo [SETUP] Creating .env file from .env.example...
    copy .env.example .env
    echo [WARNING] Please edit .env and add your OPENAI_API_KEY
    echo.
    echo Open .env with a text editor and replace:
    echo   OPENAI_API_KEY=your_openai_api_key_here
    echo with your actual API key from https://platform.openai.com/api-keys
    echo.
    pause
) else (
    echo [OK] .env file already exists
    echo.
)

REM Final message
echo ====================================
echo  Setup Complete!
echo ====================================
echo.
echo To start the application, run:
echo   python src/main.py
echo.
echo The application will be available at:
echo   http://localhost:5000
echo.
pause

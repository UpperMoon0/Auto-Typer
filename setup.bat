@echo off
echo Setting up Auto-Typer with virtual environment...
echo.

REM Check if Python is installed
py --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found!
echo.

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating virtual environment...
    py -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo Virtual environment already exists.
)

echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing required packages...
echo.
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install packages
    echo Make sure you're connected to the internet
    pause
    exit /b 1
)

echo.
echo ================================
echo Setup completed successfully!
echo ================================
echo.
echo Virtual environment is now active.
echo.
echo To run the auto-typer:
echo   py auto_typer.py
echo   or use VSCode tasks (Ctrl+Shift+P > Tasks: Run Task)
echo.
echo To activate the virtual environment manually:
echo   .venv\Scripts\activate.bat
echo.
echo Make sure to:
echo 1. Copy text to clipboard first
echo 2. Have Google Chrome installed
echo.
pause
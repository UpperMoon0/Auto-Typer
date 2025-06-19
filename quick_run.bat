@echo off
echo Quick Run Auto-Typer (Direct Python)...
echo.

REM Check if Python is installed
py --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Installing required packages globally (if needed)...
py -m pip install selenium pyperclip

echo.
echo Running auto-typer...
echo.
py auto_typer.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Script finished with errors.
    pause
)
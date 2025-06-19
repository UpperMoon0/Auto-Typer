@echo off
echo Starting Auto-Typer...
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first to create the virtual environment.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Run the auto-typer script
echo Running auto-typer...
echo.
python auto_typer.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Script finished with errors.
    pause
)
# Simple Auto-Typer - Hotkey Version

A professional Python application that types clipboard content into any input field using a global hotkey (Shift+T). Designed for bypassing paste restrictions and automating text input tasks.

## Features

- **Global Hotkey**: Activates typing of clipboard content
- **Adjustable Speed**: Press `Shift + S` to change typing speed
- **Universal Compatibility**: Works with any input field in any application or website
- **Simple Operation**: No complex setup or field selection required
- **Lightweight**: Uses minimal system resources

## Usage

### Quick Start
1. Run [`setup.bat`](setup.bat) (first time only)
2. Run [`run.bat`](run.bat) to start the application
3. Copy text to clipboard
4. Focus any input field
5. Press **Shift + T** to type

### Global Hotkeys
- **Shift + T**: Type clipboard content into focused input field
- **Shift + S**: Change typing speed (Very Fast, Fast, Normal, Slow, Custom)
- **Shift + Q**: Quit the application

## Typing Speeds

- **Very Fast**: 0.01 seconds between characters (100 chars/sec)
- **Fast**: 0.05 seconds between characters (20 chars/sec)  
- **Normal**: 0.1 seconds between characters (10 chars/sec)
- **Slow**: 0.2 seconds between characters (5 chars/sec)
- **Custom**: Set your own delay

## Installation

### Prerequisites
- **Python 3.7+** installed
- **Administrator privileges** (Windows) for global hotkeys

### Automatic Setup
```bash
# Run setup script (creates virtual environment and installs packages)
setup.bat
```

### Manual Installation
```bash
# Create virtual environment
py -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate.bat

# Install packages
pip install -r requirements.txt

# Run the application
py auto_typer.py
```

## Use Cases

This auto-typer is ideal for bypassing paste restrictions in **password fields**, **form fields**, and **text areas**, as well as for **repetitive typing tasks** and entering **long texts** manually. It is compatible with various environments, including **web browsers** (Chrome, Firefox, Edge, Safari), **desktop applications**, **text editors and IDEs**, **forms and surveys**, **chat applications**, and **command line interfaces**.

## Troubleshooting

### "Permission Denied" or Hotkeys Not Working
**Windows users**: Run as Administrator
- Right-click on `run.bat` and select "Run as administrator"
- Or run Command Prompt as admin, then execute the script

### Python Not Found
- Use `py` instead of `python` command
- Ensure Python is properly installed and added to PATH

### Missing Dependencies
```bash
# Install required packages
pip install keyboard pyautogui pyperclip

# Or use requirements file
pip install -r requirements.txt
```

### Application Stops Working
- Verify the application is still running in the background
- Check for hotkey conflicts with other applications
- Restart the application if necessary

## Security & Privacy

- **Local Operation**: No internet connection required
- **No Data Collection**: Nothing is transmitted externally
- **Open Source**: Complete transparency of functionality
- **Safe Operation**: Only types explicitly copied clipboard content

## Example Workflow

```
1. Start Auto-Typer: py auto_typer.py
2. Copy password: Ctrl+C on "MySecurePassword123"
3. Navigate to login page: Open website in browser
4. Click password field: Focus on the input
5. Press Shift+T: Automated typing begins
```

## Tips and Considerations

- The application must run continuously in the background for hotkeys to function.
- Windows users may require administrator privileges to enable global hotkeys.
- A fail-safe is enabled: move your mouse to the top-left corner of the screen to immediately stop typing.
- Keep the terminal/command window open while using the application.
- **Test thoroughly**: Verify functionality with simple text before using with sensitive data.
- **Speed optimization**: Use slower speeds for better application compatibility.
- **Focus verification**: Ensure the input field is properly focused before pressing Shift+T.



---

**License**: For educational and legitimate use only. Use responsibly and respect website terms of service.
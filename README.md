# Simple Auto-Typer - Hotkey Version

A professional Python application that types clipboard content into any input field using a global hotkey (Shift+T). Designed for bypassing paste restrictions and automating text input tasks.

## Features

- **Global Hotkey**: Press `Shift + T` to type clipboard content anywhere
- **Adjustable Speed**: Press `Shift + S` to change typing speed
- **Universal Compatibility**: Works with any input field in any application or website
- **Simple Operation**: No complex setup or field selection required
- **Lightweight**: Uses minimal system resources

## Quick Start

### Standard Setup & Run
1. Run [`setup.bat`](setup.bat) (first time only)
2. Run [`run.bat`](run.bat) to start the application
3. Copy text to clipboard
4. Focus any input field
5. Press **Shift + T** to type

## Usage Instructions

### Step-by-Step Process:
1. **Start the application**: Run `py auto_typer.py` or use the batch files
2. **Copy text**: Copy any text to your clipboard (Ctrl+C)
3. **Focus input field**: Click on any input field (website, application, etc.)
4. **Press Shift+T**: The application will type your clipboard content

### Global Hotkeys:
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

### Ideal Applications:
- **Password fields** that block paste functionality
- **Form fields** with paste restrictions
- **Text areas** that disable clipboard access
- **Any input field** in any application
- **Repetitive typing** tasks
- **Long text** that needs to be entered manually

### Compatible Environments:
- Web browsers (Chrome, Firefox, Edge, Safari)
- Desktop applications
- Text editors and IDEs
- Forms and surveys
- Chat applications
- Command line interfaces

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

## Important Notes

- The application must run continuously in the background
- Windows users may require administrator privileges for global hotkeys
- Fail-safe is enabled: move mouse to top-left corner to stop typing
- Keep the terminal/command window open while using the application

## Available Commands

```bash
# Start the application
py auto_typer.py

# Or use batch files
run.bat          # Start with virtual environment  
setup.bat        # First-time setup and installation
```

## Best Practices

- **Test thoroughly**: Verify functionality with simple text before using with sensitive data
- **Speed optimization**: Use slower speeds for better application compatibility
- **Focus verification**: Ensure the input field is properly focused before pressing Shift+T
- **Background operation**: Maintain application running for continuous hotkey functionality
- **Administrator mode**: Run as administrator on Windows for optimal compatibility

---

**License**: For educational and legitimate use only. Use responsibly and respect website terms of service.
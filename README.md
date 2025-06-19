# Simple Auto-Typer - Hotkey Version

A simple Python app that types clipboard content into any input field using a global hotkey (Shift+T). Perfect for bypassing paste restrictions!

## ✨ Features

- 🎯 **Global Hotkey**: Press `Shift + T` to type clipboard content anywhere
- ⚡ **Adjustable Speed**: Press `Shift + S` to change typing speed
- 🚀 **Universal**: Works with any input field in any application or website
- 🔧 **Simple**: No complex setup or field selection needed
- 💾 **Lightweight**: Uses minimal system resources

## 🚀 Quick Start

### Option 1: One-Click Setup & Run
1. Double-click [`setup.bat`](setup.bat) (first time only)
2. Double-click [`run.bat`](run.bat) to start the app
3. Copy text to clipboard
4. Focus any input field
5. Press **Shift + T** to type!

### Option 2: Super Quick Run
1. Double-click [`quick_run.bat`](quick_run.bat) 
2. Copy text and press **Shift + T** anywhere!

## 📋 How to Use

### Step-by-Step:
1. **Start the app**: Run `py auto_typer.py` or use the batch files
2. **Copy text**: Copy any text to your clipboard (Ctrl+C)
3. **Focus input field**: Click on any input field (website, app, etc.)
4. **Press Shift+T**: The app will type your clipboard content!

### Global Hotkeys:
- **Shift + T**: Type clipboard content into focused input field
- **Shift + S**: Change typing speed (Very Fast, Fast, Normal, Slow, Custom)
- **Shift + Q**: Quit the application

## ⚡ Typing Speeds

- **Very Fast**: 0.01 seconds between characters (100 chars/sec)
- **Fast**: 0.05 seconds between characters (20 chars/sec)  
- **Normal**: 0.1 seconds between characters (10 chars/sec)
- **Slow**: 0.2 seconds between characters (5 chars/sec)
- **Custom**: Set your own delay

## 🛠️ Installation

### Prerequisites
- **Python 3.7+** installed
- **Administrator privileges** (Windows) for global hotkeys

### Automatic Setup
```bash
# Run setup script (creates virtual environment and installs packages)
setup.bat

# Or quick install globally
quick_run.bat
```

### Manual Installation
```bash
# Create virtual environment
py -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate.bat

# Install packages
pip install -r requirements.txt

# Run the app
py auto_typer.py
```

## 🎯 Use Cases

### Perfect for:
- **Password fields** that block paste
- **Form fields** with paste restrictions
- **Text areas** that disable clipboard
- **Any input field** in any application
- **Repetitive typing** tasks
- **Long text** that needs to be entered manually

### Works everywhere:
- ✅ Web browsers (Chrome, Firefox, Edge, etc.)
- ✅ Desktop applications
- ✅ Text editors
- ✅ Forms and surveys
- ✅ Chat applications
- ✅ Command line interfaces

## 🔧 Troubleshooting

### "Permission Denied" or Hotkeys Not Working
**Windows users**: Run as Administrator
- Right-click on `run.bat` → "Run as administrator"
- Or run Command Prompt as admin, then run the script

### Python Not Found
- Use `py` instead of `python` command
- Or run [`quick_run.bat`](quick_run.bat) which handles this automatically

### Packages Missing
```bash
# Install required packages
pip install keyboard pyautogui pyperclip

# Or use requirements file
pip install -r requirements.txt
```

### App Stops Working
- Make sure it's still running in the background
- Check if hotkeys are conflicting with other apps
- Restart the application

## 🔒 Security & Privacy

- ✅ **Local only**: No internet connection required
- ✅ **No data collection**: Nothing is sent anywhere
- ✅ **Open source**: You can see exactly what it does
- ✅ **Safe**: Only types what you explicitly copy to clipboard

## 📝 Example Workflow

```
1. Start Auto-Typer: py auto_typer.py
2. Copy password: Ctrl+C on "MySecurePassword123"
3. Go to login page: Open website in browser
4. Click password field: Focus on the input
5. Press Shift+T: Watch it type automatically!
```

## ⚠️ Important Notes

- The app needs to run continuously in the background
- On Windows, you may need administrator privileges for global hotkeys
- The fail-safe is enabled: move mouse to top-left corner to stop typing
- Keep the terminal/command window open while using the app

## 🏃‍♂️ Quick Commands

```bash
# Start the app
py auto_typer.py

# Or use batch files
run.bat          # Start with virtual environment  
quick_run.bat    # Quick start without venv
setup.bat        # First-time setup
```

## 💡 Pro Tips

- **Test first**: Try with simple text before using with passwords
- **Speed matters**: Use slower speeds for better compatibility
- **Focus important**: Make sure the input field is focused before pressing Shift+T
- **Background running**: Keep the app running for continuous hotkey functionality
- **Administrator mode**: Run as admin on Windows for best compatibility

---

**License**: Educational and legitimate use only. Use responsibly and respect website terms of service.
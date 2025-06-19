import pyperclip
import time
import keyboard
import pyautogui
from threading import Thread
import sys

class SimpleAutoTyper:
    def __init__(self):
        self.running = True
        self.typing_speed = 0.05  # Default typing delay
        print("=" * 60)
        print("           SIMPLE AUTO-TYPER - HOTKEY VERSION")
        print("=" * 60)
        print("📋 HOTKEY: Press Alt + T to type clipboard content")
        print("⚡ SPEED: Press Alt + S to change typing speed")
        print("❌ EXIT: Press Alt + Q to quit")
        print("=" * 60)
        
    def get_clipboard_text(self):
        """Get text from clipboard"""
        try:
            text = pyperclip.paste()
            if text:
                return text
            else:
                print("⚠️  Clipboard is empty!")
                return None
        except Exception as e:
            print(f"❌ Error getting clipboard: {e}")
            return None
    
    def type_text_slowly(self, text):
        """Type text character by character with delay"""
        print(f"✨ Typing {len(text)} characters...")
        
        for char in text:
            # Use pyautogui to type each character
            pyautogui.write(char)
            time.sleep(self.typing_speed)
        
        print(f"✅ Successfully typed {len(text)} characters!")
    
    def change_speed(self):
        """Change typing speed interactively"""
        print("\n🚀 TYPING SPEED OPTIONS:")
        print("1. Very Fast (0.01s delay)")
        print("2. Fast (0.05s delay)")
        print("3. Normal (0.1s delay)")
        print("4. Slow (0.2s delay)")
        print("5. Custom delay")
        
        try:
            choice = input("Choose speed (1-5): ").strip()
            speed_map = {"1": 0.01, "2": 0.05, "3": 0.1, "4": 0.2}
            
            if choice in speed_map:
                self.typing_speed = speed_map[choice]
                print(f"✅ Speed set to {self.typing_speed}s delay")
            elif choice == "5":
                custom = float(input("Enter delay in seconds: "))
                self.typing_speed = custom
                print(f"✅ Speed set to {custom}s delay")
            else:
                print("❌ Invalid choice, keeping current speed")
        except ValueError:
            print("❌ Invalid input, keeping current speed")
        except KeyboardInterrupt:
            pass
    
    def on_hotkey_type(self):
        """Handle Alt+T hotkey - type clipboard content"""
        try:
            print("\n🎯 Alt+T pressed! Getting clipboard...")
            
            # Get clipboard content
            text = self.get_clipboard_text()
            if not text:
                return
            
            print(f"📋 Clipboard: {text[:50]}{'...' if len(text) > 50 else ''}")
            print("⏳ Starting to type in 2 seconds... Focus your input field!")
            
            # Give user time to focus on input field
            time.sleep(2)
            
            # Type the text
            self.type_text_slowly(text)
            
        except Exception as e:
            print(f"❌ Error during typing: {e}")
    
    def on_hotkey_speed(self):
        """Handle Alt+S hotkey - change speed"""
        print("\n⚡ Alt+S pressed! Changing speed...")
        self.change_speed()
    
    def on_hotkey_quit(self):
        """Handle Alt+Q hotkey - quit application"""
        print("\n👋 Alt+Q pressed! Exiting...")
        self.running = False
    
    def setup_hotkeys(self):
        """Setup global hotkeys"""
        try:
            # Register hotkeys
            keyboard.add_hotkey('alt+t', self.on_hotkey_type)
            keyboard.add_hotkey('alt+s', self.on_hotkey_speed)
            keyboard.add_hotkey('alt+q', self.on_hotkey_quit)
            
            print("✅ Hotkeys registered successfully!")
            print("🎯 Ready! Copy text to clipboard, focus an input field, then press Alt+T")
            
        except Exception as e:
            print(f"❌ Error setting up hotkeys: {e}")
            print("Make sure you're running as administrator if on Windows")
            return False
        
        return True
    
    def run(self):
        """Main application loop"""
        if not self.setup_hotkeys():
            return
        
        try:
            print("\n🔄 Listening for hotkeys... (Alt+Q to quit)")
            
            # Keep the application running
            while self.running:
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\n👋 Interrupted by user")
        
        finally:
            print("🧹 Cleaning up...")
            keyboard.unhook_all()
            print("✅ Goodbye!")

def main():
    """Main entry point"""
    try:
        # Check if pyautogui fail-safe is enabled
        pyautogui.FAILSAFE = True
        
        print("🚀 Starting Simple Auto-Typer...")
        
        # Create and run the auto-typer
        typer = SimpleAutoTyper()
        typer.run()
        
    except ImportError as e:
        print("❌ Missing required package!")
        print("Please install missing packages:")
        if "keyboard" in str(e):
            print("   pip install keyboard")
        if "pyautogui" in str(e):
            print("   pip install pyautogui")
        print("\nOr run: pip install -r requirements.txt")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("If you're on Windows, try running as administrator")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
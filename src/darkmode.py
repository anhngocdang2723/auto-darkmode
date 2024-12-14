import os
import time
from datetime import datetime

def is_night_time():
    """Check if the current time is between 7 PM and 7 AM."""
    current_hour = datetime.now().hour
    return current_hour >= 19 or current_hour < 7

def enable_dark_mode():
    """Enable dark mode on the laptop."""
    # This is a placeholder for the actual command to enable dark mode.
    # The implementation will vary based on the operating system.
    if os.name == 'nt':  # Windows
        os.system("powershell -command \"Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes' -Name 'Personalize' -Value 1\"")
    elif os.name == 'posix':  # macOS or Linux
        os.system("osascript -e 'tell application \"System Events\" to tell appearance preferences to set dark mode to true'")

def main():
    """Main function to check the time and enable dark mode if necessary."""
    while True:
        if is_night_time():
            enable_dark_mode()
        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    main()
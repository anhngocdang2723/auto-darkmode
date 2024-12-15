import os
import time
import ctypes
from datetime import datetime, timedelta
import subprocess
import sys

def is_admin():
    """Check if script has admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def check_windows_compatibility():
    """Check if Windows version is compatible."""
    if sys.getwindowsversion().major < 10:
        print("This script requires Windows 10 or later")
        sys.exit(1)

def is_night_time():
    """Check if current time is between 7 PM and 7 AM."""
    current_hour = datetime.now().hour
    return current_hour >= 19 or current_hour < 7

def time_until_next_check():
    """Calculate time in seconds until the next full hour."""
    now = datetime.now()
    next_check = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    return (next_check - now).total_seconds()

def enable_dark_mode_windows():
    """Enable dark mode on Windows."""
    if not is_admin():
        print("Please run this script as administrator.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    try:
        # Set dark mode for apps
        subprocess.run([
            "reg.exe",
            "add",
            "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
            "/v", "AppsUseLightTheme",
            "/t", "REG_DWORD",
            "/d", "0", "/f"
        ], check=True)

        # Set dark mode for system
        subprocess.run([
            "reg.exe",
            "add",
            "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
            "/v", "SystemUsesLightTheme",
            "/t", "REG_DWORD",
            "/d", "0", "/f"
        ], check=True)

        print("Dark mode enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable dark mode: {e}")

def main():
    """Main function to check the time and enable dark mode if necessary."""
    while True:
        if is_night_time():
            print("Nighttime detected. Enabling dark mode...")
            enable_dark_mode_windows()
        else:
            print("Daytime detected. No need for dark mode.")

        time.sleep(time_until_next_check())  # Sleep until the next check (full hour)

if __name__ == "__main__":
    check_windows_compatibility()
    if os.name == 'nt':  # Ensure the script runs only on Windows
        main()
    else:
        print("This script is designed to run only on Windows.")

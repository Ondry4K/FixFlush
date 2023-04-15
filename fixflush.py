import subprocess
import ctypes
import tkinter as tk

def execute_commands():
    # Run commands with elevated privileges
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /flushdns'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /registerdns'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /release'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /renew'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh winsock reset'"])

    # Display message box
    ctypes.windll.user32.MessageBoxW(0, "Fix done! Please restart your computer.", "Info", 0)

def main():
    # Create GUI window
    root = tk.Tk()
    root.title("FixFlush")

    # Add button to execute commands
    button = tk.Button(root, text="Click to Fix", command=execute_commands)
    button.pack(padx=10, pady=10)

    # Run GUI main loop
    root.mainloop()

if __name__ == "__main__":
    main()

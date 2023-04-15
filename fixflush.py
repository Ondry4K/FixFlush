import subprocess
import ctypes
import tkinter as tk

def execute_commands():
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /flushdns'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /registerdns'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /release'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c ipconfig /renew'"])
    subprocess.run(["powershell", "-Command", "Start-Process cmd -Verb RunAs -ArgumentList '/c netsh winsock reset'"])

    ctypes.windll.user32.MessageBoxW(0, "Fix done! Please restart your computer.", "Info", 0)

def main():
    root = tk.Tk()
    root.title("FixFlush")
    root.geometry("500x500")
    button = tk.Button(root, text="Click to fix", command=execute_commands)
    button.pack(padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import filedialog
import subprocess

def organize_downloads_default():
    subprocess.run(["python", "downloadOrg.py"])

def organize_downloads_custom():
    custom_path = filedialog.askdirectory()
    if custom_path:
        subprocess.run(["python", "downloadOrg.py", custom_path])

# Create the main window
window = tk.Tk()
window.title("Downloads Organizer")

# Create UI elements
btn_default = tk.Button(window, text="Use default location", command=organize_downloads_default)
btn_default.pack(pady=10)

btn_custom = tk.Button(window, text="Select location", command=organize_downloads_custom)
btn_custom.pack(pady=10)

# Run the UI
window.mainloop()
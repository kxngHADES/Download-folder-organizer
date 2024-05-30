import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil

# Initialize the folder_names dictionary with default mappings
folder_names = {
    ".txt": "TextFiles",
    ".pdf": "PDFFiles",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".docx": "WordFiles",
    ".xlsx": "ExcelFiles",
    ".pptx": "PowerPointFiles",
    ".mp4": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".nki": "Native Instruments",
    ".zip": "Zips",
    ".rar": "Zips",
    ".exe": "Apps",
    ".mid": "FLs",
    ".iso": "Image Discs ISO",
    ".torrent": "Torrents",
    ".fprg": "Flowgorithm"
}

def organize_downloads(custom_path=None):
    source_dir = custom_path if custom_path else os.path.join(os.path.expanduser("~"), "Downloads")

    # Create directories based on the folder_names dictionary
    for folder_name in folder_names.values():
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    files = os.listdir(source_dir)
    for file in files:
        if os.path.isfile(os.path.join(source_dir, file)):
            _, extension = os.path.splitext(file)
            if extension in folder_names:
                src_file_path = os.path.join(source_dir, file)
                dest_folder_path = os.path.join(source_dir, folder_names[extension])
                shutil.move(src_file_path, dest_folder_path)
            else:
                src_file_path = os.path.join(source_dir, file)
                dest_folder_path = os.path.join(random_folder_path, file)
                shutil.move(src_file_path, dest_folder_path)

    folders = [name for name in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, name))]
    for folder in folders:
        if folder not in folder_names.values() and folder != "Random Folders":
            src_folder_path = os.path.join(source_dir, folder)
            dest_folder_path = os.path.join(random_folder_path, folder)
            shutil.move(src_folder_path, dest_folder_path)

    status_label.config(text="Files and folders organized successfully!", foreground="green")
    messagebox.showinfo("Success", "Files and folders organized successfully!")

def organize_downloads_default():
    organize_downloads()

def organize_downloads_custom():
    custom_path = filedialog.askdirectory()
    if custom_path:
        organize_downloads(custom_path)

def add_custom_mapping():
    extension = entry_extension.get().strip()
    folder = entry_folder.get().strip()
    if extension and folder:
        if not extension.startswith("."):
            extension = f".{extension}"
        folder_names[extension] = folder
        entry_extension.delete(0, tk.END)
        entry_folder.delete(0, tk.END)
        status_label.config(text=f"Mapping added: {extension} -> {folder}", foreground="blue")
        messagebox.showinfo("Success", f"Mapping added: {extension} -> {folder}")
    else:
        status_label.config(text="Both fields must be filled out.", foreground="red")
        messagebox.showwarning("Input Error", "Both fields must be filled out.")

# Create the main window
window = tk.Tk()
window.title("Downloads Organizer")
window.geometry("400x300")

# Apply a style to the buttons and labels
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TLabel", font=("Helvetica", 10))

# Use ttk for buttons and labels
btn_default = ttk.Button(window, text="Use Default Location", command=organize_downloads_default)
btn_default.pack(pady=10)

btn_custom = ttk.Button(window, text="Select Location", command=organize_downloads_custom)
btn_custom.pack(pady=10)

# Create a frame for custom mapping with some padding
frame_custom_mapping = ttk.Frame(window, padding="10 10 10 10")
frame_custom_mapping.pack(pady=10)

ttk.Label(frame_custom_mapping, text="File Extension:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_extension = ttk.Entry(frame_custom_mapping, width=20)
entry_extension.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(frame_custom_mapping, text="Folder Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_folder = ttk.Entry(frame_custom_mapping, width=20)
entry_folder.grid(row=1, column=1, padx=5, pady=5, sticky="w")

btn_add_mapping = ttk.Button(frame_custom_mapping, text="Add Custom Folder Type", command=add_custom_mapping)
btn_add_mapping.grid(row=2, column=0, columnspan=2, pady=10)

# Status label for displaying messages to the user
status_label = ttk.Label(window, text="", font=("Helvetica", 10))
status_label.pack(pady=10)

# Run the UI
window.mainloop()

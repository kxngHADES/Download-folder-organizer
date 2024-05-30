import os
import shutil
import sys

def organize_downloads(custom_path=None):
    source_dir = custom_path if custom_path else "Downloads"

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

    for folder_name in folder_names.values():
        folder_path = os.path.join(source_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    random_folder_path = os.path.join(source_dir, "Random Folders")
    if not os.path.exists(random_folder_path):
        os.makedirs(random_folder_path)

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

    print("Files and folders organized successfully!")


if __name__ == "__main__":
    custom_path = sys.argv[1] if len(sys.argv) > 1 else None
    organize_downloads(custom_path)
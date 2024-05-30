import os
import shutil

source_dir = "C:/Users/brand/Downloads"

files = os.listdir(source_dir)

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
    ".wav" : "Music",
    ".nki": "native instraments",
    ".zip":"Zips",
    ".rar":"Zips",
    ".exe":"apps",
    ".mid": "FLs",
    ".iso":"image discs ISO",
    ".torrent":"torrents",
    ".fprg":"flowgorithm"
}

for folder_name in folder_names.values():
    folder_path = os.path.join(source_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


random_folder_path = os.path.join(source_dir, "Random Folders")
if not os.path.exists(random_folder_path):
    os.makedirs(random_folder_path)

for file in files:
    if os.path.isfile(os.path.join(source_dir, file)):
        _, exttension = os.path.splitext(file)
        if exttension in folder_names:
            src_file_path = os.path.join(source_dir, file)
            dest_folder_path = os.path.join(source_dir, folder_names[exttension])
            shutil.move(src_file_path, dest_folder_path)
        else:
            src_file_path = os.path.join(source_dir, file)
            dest_folder_path = os.path.join(source_dir, "Random Folders", file)
            shutil.move(src_file_path, dest_folder_path)


print("Files organized successfully!")
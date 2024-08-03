Open build folder and so in, in it will be the EXE run that exe and u done

# Downloads Organizer GUI

This Downloads Organizer is a desktop application that helps you organize files in your Downloads directory (or a specified directory) into categorized folders based on file types. It provides a graphical user interface (GUI) for ease of use and allows custom mappings for file extensions.

## Features

- **Organize by Default Location:** Automatically organizes files in the default Downloads directory.
- **Custom Directory Selection:** Choose a custom directory to organize files.
- **Add Custom Mappings:** Define new file extension-to-folder mappings.
- **User-Friendly Interface:** Simple and intuitive GUI using `tkinter` and `ttk`.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `shutil` and `os` libraries (included with Python standard library)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kxngHADES/Download-folder-organizer.git
   cd Download-folder-organizer
   ```

2. **Run the application:**

   Execute the script using Python:

   ```bash
   python downloads_organizer_gui.py
   ```

## Usage

1. **Launch the Application:**

   Run the script to open the application window.

2. **Organize Downloads:**

   - Click **Use Default Location** to organize files in your default Downloads folder.
   - Click **Select Location** to choose a custom directory to organize.

3. **Add Custom Mappings:**

   - Enter a file extension (e.g., `.csv`) and a folder name (e.g., `CSVFiles`) in the respective fields.
   - Click **Add Custom Folder Type** to save the mapping.

4. **View Status:**

   - Check the status label at the bottom for success messages and error warnings.

## Default Mappings

The application organizes files into the following default categories:

- **TextFiles:** `.txt`
- **PDFFiles:** `.pdf`
- **Images:** `.jpg`, `.jpeg`, `.png`
- **WordFiles:** `.docx`
- **ExcelFiles:** `.xlsx`
- **PowerPointFiles:** `.pptx`
- **Videos:** `.mp4`
- **Music:** `.mp3`, `.wav`
- **Native Instruments:** `.nki`
- **Zips:** `.zip`, `.rar`
- **Apps:** `.exe`
- **FLs:** `.mid`
- **Image Discs ISO:** `.iso`
- **Torrents:** `.torrent`
- **Flowgorithm:** `.fprg`

Files with extensions not listed above are placed in a folder named `Random Folders`.

## Customization

You can modify the default mappings by editing the `folder_names` dictionary within the script:

```python
folder_names = {
    ".txt": "TextFiles",
    ".pdf": "PDFFiles",
    # Add more extensions and folder names as needed
}
```

## Notes

- Ensure you have the necessary permissions to move files within the selected directory.
- Files are moved, not copied, so use the application with caution to avoid unintended file displacement.

## License

This project is open source and available under the MIT License.

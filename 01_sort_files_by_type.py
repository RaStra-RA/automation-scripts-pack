# 01_sort_files_by_type.py
# Sort files into folders based on their extension

import shutil
from pathlib import Path

def main():
    print("File type sorter")

    folder_text = input("Enter folder path (empty for current folder): ").strip()
    if folder_text:
        folder = Path(folder_text)
    else:
        folder = Path(".")

    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist")
        return

    count = 0

    for entry in folder.iterdir():
        if entry.is_file():
            ext = entry.suffix.lower().replace(".", "")
            if not ext:
                ext = "no_extension"

            target_folder = folder / ext
            target_folder.mkdir(exist_ok=True)

            new_path = target_folder / entry.name
            try:
                shutil.move(str(entry), str(new_path))
                count += 1
            except Exception as e:
                print("Skip", entry.name, "-", e)

    print("Sorted", count, "files in", folder)

if __name__ == "__main__":
    main()

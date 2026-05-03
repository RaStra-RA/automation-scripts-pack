# 02_rename_photos_by_date.py
# Rename photos by EXIF date or file modified date

from pathlib import Path
from datetime import datetime

try:
    from PIL import Image
except ImportError:
    print("This script needs the Pillow library.")
    print("Install it with: pip install Pillow")
    exit(1)

def get_exif_date(path: Path):
    try:
        img = Image.open(path)
        exif = img._getexif()
        if not exif:
            return None
        date_str = exif.get(36867)  # DateTimeOriginal
        if date_str:
            return datetime.strptime(date_str, "%Y:%m:%d %H:%M:%S")
    except Exception:
        return None
    return None

def main():
    print("Rename photos by date")

    folder_text = input("Enter folder path with photos (empty for current): ").strip()
    if folder_text:
        folder = Path(folder_text)
    else:
        folder = Path(".")

    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist")
        return

    count = 0

    for entry in folder.iterdir():
        if entry.is_file() and entry.suffix.lower() in {".jpg", ".jpeg", ".png"}:

            date = get_exif_date(entry)
            if not date:
                ts = entry.stat().st_mtime
                date = datetime.fromtimestamp(ts)

            base_name = date.strftime("%Y-%m-%d_%H-%M-%S")
            new_name = base_name + entry.suffix.lower()
            new_path = entry.with_name(new_name)

            num = 1
            while new_path.exists():
                new_name = f"{base_name}_{num}{entry.suffix.lower()}"
                new_path = entry.with_name(new_name)
                num += 1

            try:
                entry.rename(new_path)
                count += 1
            except Exception as e:
                print("Skip", entry.name, "-", e)

    print("Renamed", count, "photos in", folder)

if __name__ == "__main__":
    main()

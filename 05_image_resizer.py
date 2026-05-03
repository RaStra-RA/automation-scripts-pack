# 05_image_resizer.py
# Resize all images in folder to a target width

from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("This script needs the Pillow library.")
    print("Install it with: pip install Pillow")
    exit(1)

def main():
    print("Image resizer")

    folder_text = input("Enter folder path with images (empty for current): ").strip()
    if folder_text:
        folder = Path(folder_text)
    else:
        folder = Path(".")

    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist")
        return

    width_text = input("Enter target width in pixels (example: 800): ").strip()
    if not width_text.isdigit():
        print("Invalid width")
        return

    target_width = int(width_text)
    count = 0

    for entry in folder.iterdir():
        if entry.is_file() and entry.suffix.lower() in {".jpg", ".jpeg", ".png"}:
            try:
                img = Image.open(entry)
                w, h = img.size
                if w <= target_width:
                    print("Skip", entry.name, "- already smaller than target width")
                    continue
                new_height = int(h * (target_width / w))
                resized = img.resize((target_width, new_height))
                resized.save(entry)
                count += 1
            except Exception as e:
                print("Skip", entry.name, "-", e)

    print("Resized", count, "images in", folder)

if __name__ == "__main__":
    main()

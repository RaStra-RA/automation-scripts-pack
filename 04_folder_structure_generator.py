# 04_folder_structure_generator.py

from pathlib import Path

def main():
    print("Folder structure generator")

    base_text = input("Enter the name of the folder to create: ").strip()

    if not base_text:
        print("Folder name is required")
        return

    base = Path(base_text)

    try:
        base.mkdir(parents=True, exist_ok=False)
        print(f"Folder '{base}' created successfully.")
    except FileExistsError:
        print(f"Folder '{base}' already exists.")

    subfolders = [
        "images",
        "videos",
        "documents",
        "audio",
        "backup",
        "temp",
    ]

    for sub in subfolders:
        sub_path = base / sub
        sub_path.mkdir(exist_ok=True)

    print("Subfolders created inside", base)

if __name__ == "__main__":
    main()

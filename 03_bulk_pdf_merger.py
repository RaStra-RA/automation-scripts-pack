# 03_bulk_pdf_merger.py
# Merge several PDF files into one output PDF

from pathlib import Path

try:
    from PyPDF2 import PdfMerger
except ImportError:
    print("This script needs the PyPDF2 library.")
    print("Install it with: pip install PyPDF2")
    exit(1)

def main():
    print("Bulk PDF merger")

    folder_text = input("Enter folder path with PDFs (empty for current): ").strip()
    if folder_text:
        folder = Path(folder_text)
    else:
        folder = Path(".")

    if not folder.exists() or not folder.is_dir():
        print("Folder does not exist")
        return

    output_name = input("Enter output PDF name (example: merged.pdf): ").strip()
    if not output_name:
        print("Output name is required")
        return
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    merger = PdfMerger()
    count = 0

    pdf_files = sorted(folder.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found in", folder)
        return

    for pdf in pdf_files:
        try:
            merger.append(str(pdf))
            count += 1
        except Exception as e:
            print("Skip", pdf.name, "-", e)

    if count == 0:
        print("No PDFs were merged")
        return

    try:
        output_path = folder / output_name
        merger.write(str(output_path))
        merger.close()
        print("Merged", count, "PDF files into", output_path)
    except Exception as e:
        print("Error while saving merged PDF:", e)

if __name__ == "__main__":
    main()


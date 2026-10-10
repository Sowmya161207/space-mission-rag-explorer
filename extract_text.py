from pypdf import PdfReader

pdf_path = "data/Chandrayaan-3.pdf"

reader = PdfReader(pdf_path)

print("Number of pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()

    if text:
        print(text)
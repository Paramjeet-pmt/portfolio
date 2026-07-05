import os
import pypdf
pdf_path = r'c:\Users\param\Downloads\My Resume (1).pdf'
print('exists', os.path.exists(pdf_path))
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print('pages', len(reader.pages))
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    print(text)

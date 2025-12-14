import os
import pypdf
import docx

def read_file(file_path: str) -> str:
    """
    Reads the content of a file based on its extension.
    Supports .md, .txt, .pdf, .docx
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext in ['.md', '.txt']:
        return _read_text(file_path)
    elif ext == '.pdf':
        return _read_pdf(file_path)
    elif ext == '.docx':
        return _read_docx(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def _read_text(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def _read_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def _read_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

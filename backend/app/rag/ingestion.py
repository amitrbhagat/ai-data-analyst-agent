from pypdf import PdfReader
from pathlib import Path



def load_documents(directory_path: str) -> list[dict]:
    
    directory = Path(directory_path)

    if not directory.exists():
        raise FileNotFoundError(
            f"Document directory does not exist: {directory_path}"
        )

    if not directory.is_dir():
        raise ValueError(
            f"Provided path is not a directory: {directory_path}"
        )

    documents = []

    pdf_files = sorted(directory.glob("*.pdf"))

    for pdf_path in pdf_files:
        reader = PdfReader(pdf_path)

        pages_text = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages_text.append(text)

        full_text = "\n".join(pages_text).strip()

        if not full_text:
            print(f"Warning: No text extracted from {pdf_path.name}")
            continue

        documents.append({
            "text": full_text,
            "source_filename": pdf_path.name,
        })  

    return documents              

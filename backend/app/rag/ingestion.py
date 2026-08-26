from pypdf import PdfReader
from pathlib import Path

from app.rag.chunking import chunk_text
from app.rag.embeddings import get_embeddings
from app.rag.vector_store import add_documents




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





def run_ingestion_pipeline():

    # Path to the PDF documents
    documents_path = Path(__file__).resolve().parents[3] / "rag_data" / "documents"

    # Step 1: Load PDF documents
    documents = load_documents(str(documents_path))

    if not documents:
        print("No documents found.")
        return

    total_chunks = 0


    all_chunks = []
    all_embeddings = []
    all_metadatas = []
    all_ids = []

    for document in documents:

        text = document["text"]
        source_filename = document["source_filename"] 

        chunks = chunk_text(text)

        print(
            f"{source_filename}: "
            f"created {len(chunks)} chunks"
        )

        if not chunks:
            continue

        embeddings = get_embeddings(chunks)

        for index, chunk in enumerate(chunks):

            all_chunks.append(chunk)
            all_embeddings.append(embeddings[index])

            all_metadatas.append({
                "source_filename": source_filename,
                "chunk_index": index,
            })

            all_ids.append(
                f"{source_filename}-{index}"
            )   

        total_chunks += len(chunks)


    add_documents(
        chunks=all_chunks,
        embeddings=all_embeddings,
        metadatas = all_metadatas,
        ids = all_ids,
    )


    print()
    print("===================================")
    print("RAG INGESTION COMPLETED")
    print("===================================")
    print(f"Documents processed: {len(documents)}")
    print(f"Total chunks: {total_chunks}")
    print("Embeddings generated successfully.")
    print("Chunks stored in ChromaDB.")
    print("===================================")




if __name__ == "__main__":
    run_ingestion_pipeline()



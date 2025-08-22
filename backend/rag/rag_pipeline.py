import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.documents import Document
from typing import List, Optional
from rag.chunking import chunk_documents
from pathlib import Path


def load_documents(data_dir: Optional[str] = None) -> List[Document]:
    """
    Loads all PDF files from the specified directory (or ./data by default),
    and adds clean metadata (filename, page number, chunk_version) to each page-level Document.
    """
    # Resolve a default data path relative to this file
    base = Path(__file__).resolve().parent.parent
    data_path = Path(data_dir) if data_dir else base / "data"

    # Load all PDFs in that folder
    loader = DirectoryLoader(
        str(data_path),
        glob="**/*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True
    )
    documents = loader.load()

    # Clean metadata and add versioning
    for doc in documents:
        filename = Path(doc.metadata["source"]).name
        doc.metadata["source"] = filename
        doc.metadata["chunk_version"] = "v1"

    return documents

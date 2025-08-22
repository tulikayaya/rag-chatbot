# rag/chunking.py
from langchain_text_splitters import TokenTextSplitter, RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

def chunk_documents(
    documents: List[Document],
    header_pattern: str = r"(?m)^(?:\d+(?:\.\d+)+)\s+.+$",
    token_chunk_size: int = 1000,
    token_chunk_overlap: int = 200,
    fine_chunk_size: int = 800,
    fine_chunk_overlap: int = 200,
) -> List[Document]:
    """
    Hierarchical chunking strategy:
    1) Split on section headers using a regex (e.g., 1.0, 2.3.1)
    2) Token-based splitting within each section
    3) Recursive regex fallback for any oversized chunks
    """

    # ----- STAGE 1: Header-based regex split -----
    header_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,  # large enough to avoid chunk-size based splits
        chunk_overlap=0,
        separators=[header_pattern],
        is_separator_regex=True
    )
    sections = header_splitter.split_documents(documents)

    # ----- STAGE 2: Token-based chunking -----
    token_splitter = TokenTextSplitter(
        chunk_size=token_chunk_size,
        chunk_overlap=token_chunk_overlap
    )
    token_chunks = token_splitter.split_documents(sections)

    # ----- STAGE 3: Fallback recursive character split for large token chunks -----
    fine_splitter = RecursiveCharacterTextSplitter(
        chunk_size=fine_chunk_size,
        chunk_overlap=fine_chunk_overlap,
        separators=[r'\n\n', r'\n', r'(?<=[.?!])\s+', ' ', ''],
        is_separator_regex=True
    )
    
    final_chunks: List[Document] = []
    for chunk in token_chunks:
        if len(chunk.page_content) > 2 * token_chunk_size:
            final_chunks.extend(fine_splitter.split_documents([chunk]))
        else:
            final_chunks.append(chunk)

    return final_chunks

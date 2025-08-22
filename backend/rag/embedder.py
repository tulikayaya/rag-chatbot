import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone

# we load .env variables at the get-go so that the rest of the file can read them
load_dotenv()

def get_embedder():
    """
    Initialize and return an OpenAIEmbeddings instance using our API key.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    return OpenAIEmbeddings(openai_api_key=api_key)

def embed_and_store(chunks):
    """
    Embed a list of Document chunks and upsert them into Pinecone.
    Each chunk’s metadata (source, page, chunk_version) is preserved.
    """
    embedder = get_embedder()
    Pinecone.from_documents(
        documents=chunks,
        embedding=embedder,
        index_name=os.getenv("PINECONE_INDEX_NAME")
    )

if __name__ == "__main__":
    from rag.rag_pipeline import chunk_documents, load_documents

    docs = load_documents()
    chunks = chunk_documents(docs)
    print(f"Embedding & storing {len(chunks)} chunks…")
    embed_and_store(chunks)
    print("✅ Done!")

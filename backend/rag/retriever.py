import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Pinecone
from langchain_community.embeddings import OpenAIEmbeddings
#from pinecone import Pinecone as PineconeClient
from pinecone import Pinecone

# Step 1: Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX = os.getenv("PINECONE_INDEX_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 2: Initialize embedding model (must match the one used in embedder.py)
embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Step 3: Connect to Pinecone client and get index handle
#pc = PineconeClient(api_key=PINECONE_API_KEY)
#index = pc.Index(PINECONE_INDEX)

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

# Step 4: Set up retriever from LangChain's Pinecone wrapper
def get_retriever(top_k: int = 10):
    """
    Returns a retriever object that can fetch top-k similar chunks from Pinecone
    based on semantic similarity using OpenAI embeddings.
    """
    vectorstore = Pinecone(
        index=index,
        embedding=embedding_model,
        text_key="text"
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})
    return retriever

# Optional test
#if __name__ == "__main__":
#    retriever = get_retriever()
#    query = "How do I document the informed consent process?"
#    results = retriever.get_relevant_documents(query)

#    for i, doc in enumerate(results, 1):
#        print(f"\nResult {i}")
#        print("📄", doc.page_content[:300])
#        print("📎 Metadata:", doc.metadata)

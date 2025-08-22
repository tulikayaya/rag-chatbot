from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()  # Load your .env variables

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

# ⚠️ Delete ALL vectors from the index
index.delete(delete_all=True)

print(f"✅ Cleared all vectors from index: {PINECONE_INDEX}")

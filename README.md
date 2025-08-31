# RAG-Chatbot: Clinical Research Assistant

This Retrieval-Augmented Generation (RAG) chatbot answers clinical research queries using institutional policy documents. Built using LangChain, Pinecone, and OpenAI's GPT-4, it provides accurate and context-aware responses grounded in real data.

## Use Case

Designed for research coordinators, clinical trial staff, and administrative teams, this chatbot helps surface relevant SOPs, policies, and procedures from internal documentation—reducing manual lookup time and improving compliance adherence.

---

## Tech Stack

| Layer         | Technology                          |
|---------------|--------------------------------------|
| LLM           | OpenAI GPT-4 (`langchain-openai`)    |
| Embedding     | `text-embedding-3-small`             |
| Vector Store  | Pinecone                             |
| Chunking      | RecursiveCharacterTextSplitter       |
| Backend       | FastAPI                              |
| Deployment    | Railway (backend), Vercel (frontend) |
| DevOps        | GitHub Actions, Docker               |

---

---

## RAG Pipeline

### 1. Preprocessing
Documents are preprocessed using a **custom recursive chunking strategy** that balances semantic boundaries and chunk length, ensuring each chunk is rich enough for standalone retrieval while avoiding token overflows.

### 2. Embedding
Each chunk is embedded via OpenAI’s `text-embedding-3-small` model.

### 3. Vector Storage
Embeddings and custom chunk metadata (e.g., `source`, `page_number`, `chunk_index`, etc.) are stored in Pinecone for efficient vector retrieval using cosine similarity.

### 4. Retrieval-Augmented QA
- A user query triggers semantic search in Pinecone.
- Top-matching document chunks are fetched.
- The user query + retrieved chunks are passed to GPT-4 via LangChain.
- GPT-4 generates a grounded answer with supporting citations.

---

## Deleting `/data` Does Not Affect Chatbot

All PDFs in `/data/` have been removed from this repo to keep it lightweight and clean. Since documents are already parsed and embedded into Pinecone, chatbot functionality is unaffected.

---

## Running Locally

```bash
# Clone the repo
git clone https://github.com/tulikayaya/rag-chatbot.git
cd rag-chatbot/backend

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env  # then edit .env with your keys

# Run the FastAPI server
uvicorn main:app --reload


# Run the FastAPI server
uvicorn main:app --reload

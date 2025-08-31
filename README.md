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
PDF documents were parsed and split into overlapping chunks using `RecursiveCharacterTextSplitter`, ensuring semantic coherence and retrievability.

### 2. Embedding
Each chunk was embedded via OpenAI’s `text-embedding-3-small` model.

### 3. Vector Storage
Embeddings and chunk metadata (e.g. source, page number) were stored in Pinecone for fast cosine similarity retrieval.

### 4. Retrieval-Augmented QA
- A user query triggers a Pinecone search for the most relevant chunks.
- Retrieved chunks and the user question are passed to GPT-4 via LangChain.
- The chatbot generates a grounded, reference-based response.

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

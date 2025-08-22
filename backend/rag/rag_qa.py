import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from rag.rag_pipeline import load_documents
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from rag.retriever import get_retriever

# Step 1: Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Step 2: Set up the LLM (GPT-4 or GPT-3.5)
llm = ChatOpenAI(
    model="gpt-4",  # You can also use "gpt-3.5-turbo"
    temperature=0,
    api_key=OPENAI_API_KEY
)

# Step 3: Prompt template for final answer generation
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant. Answer the question using ONLY the context below. When referencing a source, include the filename and page number if available."),
    ("human", "Context:\n\n{context}\n\nQuestion: {question}")
])


# Step 4: Format the final LLM input and run the RAG pipeline
def answer_query(query: str, k: int = 10) -> str:
    """
    Runs the full RAG pipeline:
    - Retrieves top-k documents using semantic similarity
    - Injects them into a prompt
    - Calls GPT-4 to generate a final answer
    """
    retriever = get_retriever(top_k=k)
    docs: list[Document] = retriever.get_relevant_documents(query)

    # Combine all document chunks into one big context string
    context = ""
    for doc in docs:
        source = doc.metadata.get("source", "Unknown file")
        page = doc.metadata.get("page", "N/A")
        context += f"(Source: {os.path.basename(source)}, Page: {page})\n{doc.page_content}\n\n"



    # Format the full prompt using your template
    chain = prompt | llm  # Pipe prompt → LLM
    response = chain.invoke({
        "context": context,
        "question": query
    })

    return response.content

# Optional CLI test
#if __name__ == "__main__":
#    user_q = input("🧠 Enter your question: ")
#    answer = answer_query(user_q)
#    print("\n💬 Answer:\n", answer)

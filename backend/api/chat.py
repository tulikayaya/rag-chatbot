from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
#from rag.retriever import get_retriever
from rag.rag_qa import answer_query

router = APIRouter()
#retriever = get_retriever()

class QuestionRequest(BaseModel):
    question: str

@router.post("/chat")
async def chat(request: QuestionRequest):
    try:
        answer = answer_query(request.question) #retriever
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


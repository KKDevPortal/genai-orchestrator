from fastapi import APIRouter
from app.models import QuestionRequest, AnswerResponse
from app.orchestrator import handle_question

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    answer = handle_question(req.question)
    return AnswerResponse(answer=answer)

@router.get("/health")
def health_check():
    return {"status": "ok"}

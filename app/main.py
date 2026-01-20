from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="GenAI Orchestrator",
    description="Orchestration service for ChatGPT-based workflows",
    version="1.0.0"
)

app.include_router(router)
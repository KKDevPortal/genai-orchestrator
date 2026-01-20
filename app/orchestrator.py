from app.llm_client import chat_completion

def handle_question(question: str) -> str:
    # Task-1
    if len(question.split()) < 15:
        strategy = "simple"
    else:
        strategy = "detailed"
    
    # Task-2
    if strategy == "simple":
        prompt = f"Answer clearly:\n {question}"
    else:
        prompt = f"""
        you are a expert assistant.
        Provide a structured, detailed answer with examples.
        
        Question:
        {question}
        """
    
    # Task-3
    response = chat_completion(prompt)
    
    # Task-4
    return response.strip()
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages: List[str]
    allow_search: bool




from fastapi import FastAPI
ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]



app=FastAPI(titel="Langgraph Ai Agent")
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return{"error": "Invalid Model name.Kindly Select valid Ai agent"}
    
    llm_id=request.model_name
    query=request.messages
    allow_search=request.allow_search
    system_prompt=request.system_prompt
    provider=request.model_provider
    

    response=get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response
    

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.01",port=9999)
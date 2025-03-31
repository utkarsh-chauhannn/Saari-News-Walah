import os
import logging
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


logging.basicConfig(level=logging.INFO)


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    """Generates a response from the AI agent with optional web search"""
    
    logging.info("Received request: %s", {"llm_id": llm_id, "allow_search": allow_search, "provider": provider})
    
    
    if provider not in ["Groq", "OpenAI"]:
        logging.error("Invalid provider specified: %s", provider)
        return {"error": "Invalid provider specified. Choose either 'Groq' or 'OpenAI'."}

    
    try:
        llm = ChatGroq(model=llm_id) if provider == "Groq" else ChatOpenAI(model=llm_id)
    except Exception as e:
        logging.error("Failed to initialize LLM: %s", str(e))
        return {"error": "Failed to initialize LLM."}

    
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    
    try:
        agent = create_react_agent(
            model=llm,
            tools=tools,
            state_modifier=system_prompt
        )
    except Exception as e:
        logging.error("Error creating AI agent: %s", str(e))
        return {"error": "Failed to create AI agent."}
    
    
    state = {"messages": query}
    try:
        response = agent.invoke(state)
    except Exception as e:
        logging.error("Error invoking AI agent: %s", str(e))
        return {"error": "Failed to process request with AI agent."}
    
    
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]

    
    if not ai_messages:
        logging.warning("AI did not generate a response.")
        return {"error": "AI did not generate a response."}
    
    ai_response = ai_messages[-1]  
    logging.info("AI Response: %s", ai_response)
    return {"response": ai_response}
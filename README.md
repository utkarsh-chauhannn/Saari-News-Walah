# **NewsWaalah 📰**  
**End-to-End AI-Powered Chatbot with FastAPI, LangGraph, LangChain, and Streamlit**  

## 📌 Overview  
NewsWaalah is an AI-powered chatbot designed to provide intelligent news-related assistance. Built with **FastAPI**, **LangGraph**, **LangChain**, and **Streamlit**, it integrates various tools to deliver insightful responses and fetch real-time news data. The chatbot uses **LangChain's ReAct (Reasoning + Acting) framework** to interact with multiple APIs and generate informative replies.  

---

## 🚀 Features  
- **LangChain-Powered AI Agent**: Uses **Groq's LLaMA** models & **Tavily Search** for real-time information retrieval.  
- **FastAPI Backend**: Handles API requests, validates data using **Pydantic**, and provides API documentation via **Swagger UI**.  
- **Streamlit Frontend**: User-friendly chat interface for interacting with the AI chatbot.  
- **LangGraph for AI Workflow**: Implements a structured **ReAct agent** (Reasoning + Action) for dynamic responses.  
- **Modular & Scalable**: Designed for easy expansion with additional tools and models.  

---

## 🏗️ Project Layout  

### **Phase 1 – AI Agent Development (LangChain & LangGraph)**  
✅ Setup **API Keys** for OpenAI, Groq & Tavily  
✅ Configure **LangChain LLMs (Groq, OpenAI) & Tools (Tavily Search)**  
✅ Implement **ReAct Agent** using LangChain & LangGraph  

### **Phase 2 – Backend Setup (FastAPI + LangChain Integration)**  
✅ Define **Pydantic models** for request validation  
✅ Integrate AI Agent into FastAPI endpoints  
✅ Test API with **Swagger UI** and FastAPI interactive docs  

### **Phase 3 – Frontend Setup (Streamlit UI)**  
✅ Design **interactive chat UI** using Streamlit  
✅ Connect frontend with FastAPI backend  
✅ Enable smooth AI-powered responses  

---

## 🔧 Installation & Usage  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/newswaalah.git  
cd newswaalah  

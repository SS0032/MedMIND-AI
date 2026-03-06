# 🧠 MindGuard AI (MedChat AI)

An AI-powered mental health assistant that provides conversational support, answers medical questions using document-based knowledge (RAG), and triggers emergency alerts via SMS and phone call when crisis signals are detected.

The system uses **Google Gemini**, **LangChain**, **FAISS**, and **Streamlit** to create a real-time interactive AI assistant.

---

# 🚀 Features

### 🤖 AI Mental Health Chatbot
- Conversational AI powered by **Google Gemini**
- Provides supportive responses to mental health queries
- Maintains conversation context

### 📄 PDF-Based Knowledge (RAG)
- Upload medical PDFs
- Ask questions based on document content
- Uses **FAISS vector database** and **sentence-transformers**

### 🚨 Emergency Detection System
Detects crisis keywords like:
- suicide
- kill myself
- I want to die
- depressed

When detected, the system:

✔ Sends **SMS alert via Twilio**  
✔ Initiates **automated emergency phone call**  
✔ Displays **therapist contacts and helplines**

### 📞 Emergency Contact Support
Shows therapist details and mental health helplines.

### 💬 ChatGPT-like Interface
Built using **Streamlit chat UI** for continuous conversations.

---

# 🏗️ Tech Stack

**Frontend**
- Streamlit

**AI / LLM**
- Google Gemini API

**AI Framework**
- LangChain
- LangGraph

**RAG System**
- FAISS Vector Database
- Sentence Transformers
- PyPDF

**Backend**
- Python

**Emergency System**
- Twilio (SMS + Voice Call)

---

# 📂 Project Structure

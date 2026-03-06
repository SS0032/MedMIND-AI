# 🧠 MedMIND-AI

**MedMIND-AI** is an AI-powered mental health assistant that provides supportive conversations, answers medical queries using document-based knowledge (RAG), and triggers emergency alerts when crisis signals are detected.

The system integrates **Google Gemini**, **LangChain**, **FAISS**, **Streamlit**, and **Twilio** to deliver a real-time conversational AI experience with safety mechanisms for mental health crises.

---

# 🚀 Features

## 🤖 AI Mental Health Chatbot

* Conversational assistant powered by **Google Gemini**
* Provides supportive responses to mental health concerns
* Continuous chat interface similar to ChatGPT

## 📄 PDF-Based Medical Knowledge (RAG)

* Upload medical or research PDFs
* Ask questions based on document content
* Uses **Retrieval Augmented Generation (RAG)** with FAISS

## 🚨 Crisis Detection & Emergency Alerts

Detects crisis-related phrases such as:

* "suicide"
* "kill myself"
* "I want to die"
* "I feel like dying"

When detected, the system:

✔ Sends **SMS alert using Twilio**
✔ Initiates **automated emergency phone call**
✔ Displays **therapist contacts and helplines**

## 📞 Emergency Support Information

Shows mental health resources including:

* Therapist contacts
* Crisis helplines
* Supportive guidance

## 💬 Chat-Based User Interface

Built using **Streamlit** for an interactive chat experience.

---

# 🏗️ Tech Stack

### Frontend

* Streamlit

### AI Model

* Google Gemini API

### AI Framework

* LangChain
* LangGraph

### RAG System

* FAISS Vector Database
* Sentence Transformers
* PyPDF Loader

### Backend

* Python

### Emergency Notification

* Twilio (SMS + Voice Call)

---

# 📂 Project Structure

```
MedMIND-AI/
│
├── frontend.py
├── requirements.txt
├── .env
│
└── backend/
    ├── ai_agent.py
    ├── rag.py
    ├── memory.py
    ├── config.py
    └── tools.py
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/MedMIND-AI.git
cd MedMIND-AI
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
USER_PHONE_NUMBER=your_phone_number
```

---

# ▶️ Run the Application

Start the Streamlit app:

```
streamlit run frontend.py
```

Then open:

```
http://localhost:8501
```

---

# 📄 How PDF RAG Works

1. Upload a PDF document
2. Enable **Use PDF RAG**
3. Ask questions related to the document

The system:

* Splits the PDF into text chunks
* Converts them to embeddings
* Stores them in a FAISS vector database
* Retrieves relevant chunks to answer queries

---

# 🚨 Emergency Alert Workflow

```
User Message
     ↓
Crisis Keyword Detection
     ↓
Twilio SMS Alert Sent
     ↓
Twilio Emergency Phone Call Triggered
     ↓
Therapist Contacts & Helplines Displayed
```

---

# ⚠️ Disclaimer

This project is intended for **educational and research purposes only**.

MedMIND-AI does **not replace professional mental health care or medical advice**. If you are experiencing a crisis, please contact a qualified professional or emergency services immediately.

---

# 🌟 Future Improvements

* Emotion detection using advanced NLP models
* Real-time therapist discovery using Google Maps API
* Voice-based AI interaction
* WhatsApp emergency alerts
* Multi-document RAG system
* Persistent vector database storage

---

# 👨‍💻 Author

**Sahil Singh**

AI & Data Science Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

import google.generativeai as genai

from backend.config import GEMINI_API_KEY
from backend.memory import Memory
from backend.rag import RAG
from backend.tools import (
    send_emergency_alert,
    make_emergency_call,
    get_emergency_contacts
)


class AIAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

        self.memory = Memory()
        self.rag = RAG()

    def get_response(self, query, use_rag=False):
        try:
            query_lower = query.lower()

            # 🚨 Emergency Detection
            if any(x in query_lower for x in [
                "suicide",
                "kill myself",
                "hurt myself",
                "end my life",
                "i want to die",
                "i feel like dying",
                "i want to end it all",
                "killing myself",
                "dying",
                "suicidal thoughts",
                "suicidal"

            ]):
                sms_status = send_emergency_alert()
                call_status = make_emergency_call()
                contacts = get_emergency_contacts()

                return f"""
🚨 I’m really sorry you're feeling this way. You’re not alone.

{contacts}

{sms_status}
{call_status}

💙 Please consider reaching out to someone you trust. I'm here to talk as well.
"""

            # 📄 RAG Mode
            if use_rag:
                context = self.rag.query(query)
                prompt = f"""
You are a helpful medical assistant.

Use the following context to answer the question.

Context:
{context}

Question: {query}
"""
            else:
                prompt = query

            # 🤖 Generate response
            response = self.model.generate_content(prompt)

            if not response.text:
                return "⚠️ No response from Gemini"

            # 🧠 Store memory
            self.memory.add(query, response.text)

            return response.text

        except Exception as e:
            return f"❌ ERROR: {str(e)}"
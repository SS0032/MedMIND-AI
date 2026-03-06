import streamlit as st
from backend.ai_agent import AIAgent

st.set_page_config(page_title="MedChat AI")

# ✅ Persist agent + chat
if "agent" not in st.session_state:
    st.session_state.agent = AIAgent()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

agent = st.session_state.agent

st.title("🧠 MedChat AI")

# ✅ RAG toggle
use_rag = st.checkbox("Use PDF RAG")

# ✅ PDF Upload
uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    agent.rag.load_pdf("temp.pdf")
    st.success("PDF loaded!")

# ✅ Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["user"])
    with st.chat_message("assistant"):
        st.write(chat["bot"])

# ✅ Chat input (modern UI)
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response
    response = agent.get_response(user_input, use_rag)

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(response)

    # Save history
    st.session_state.chat_history.append({
        "user": user_input,
        "bot": response
    })
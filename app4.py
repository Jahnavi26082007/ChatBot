import streamlit as st
import ollama
import json
import os
import uuid
FILE = "chats.json"
def load_chats():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}
def save_chats(chats):
    with open(FILE, "w") as f:
        json.dump(chats, f, indent=4)
chats = load_chats()
if "current_chat" not in st.session_state:
    if chats:
        st.session_state.current_chat = list(chats.keys())[-1]
    else:
        chat_id = str(uuid.uuid4())
        chats[chat_id] = {
            "name": "New Chat",
            "messages": []
        }
        save_chats(chats)
        st.session_state.current_chat = chat_id
st.sidebar.title("💬 My Chats")
if st.sidebar.button("➕ New Chat"):
    chat_id = str(uuid.uuid4())
    chats[chat_id] = {
        "name": "New Chat",
        "messages": []
    }
    save_chats(chats)
    st.session_state.current_chat = chat_id
    st.rerun()
st.sidebar.subheader("Previous Chats")
for chat_id, chat in chats.items():
    if st.sidebar.button(
        chat["name"],
        key=chat_id
    ):
        st.session_state.current_chat = chat_id
        st.rerun()
current_id = st.session_state.current_chat
current_chat = chats[current_id]
st.title("🤖 Ollama AI Chatbot")
st.caption("Current Chat: " + current_chat["name"])
for message in current_chat["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])
prompt = st.chat_input("Type your message...")
if prompt:
    current_chat["messages"].append({
        "role": "user",
        "content": prompt
    })
    if current_chat["name"] == "New Chat":
        current_chat["name"] = prompt[:30]
    save_chats(chats)
    with st.chat_message("user"):
        st.write(prompt)
    response = ollama.chat(
        model="llama3.2",
        messages=current_chat["messages"]
    )
    answer = response["message"]["content"]
    with st.chat_message("assistant"):
        st.write(answer)
    current_chat["messages"].append({
        "role": "assistant",
        "content": answer
    })
    save_chats(chats)
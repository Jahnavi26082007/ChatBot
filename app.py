import streamlit as st
import ollama

st.title("🤖 Welcome to AI Chatbot")

user_input = st.text_input("Ask your question:")

if st.button("Generate"):
    if user_input:
        st.success("Answer generated successfully!")

        st.write("Your Input:")
        st.write(user_input)

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        st.write("Required Output:")
        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a question.")
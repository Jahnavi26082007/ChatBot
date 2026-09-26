import streamlit as st
st.title("Welcome to AI Chatbot")
user_input = st.text_input("Enter your question:")
if st.button("Generate"):
    if user_input:
        st.success("Response generated successfully!")
        st.write("Your Input:")
        st.write(user_input)
        st.write("Required Output:")
        st.write("This is the AI response for your input.")
    else:
        st.warning("Please enter something first.")
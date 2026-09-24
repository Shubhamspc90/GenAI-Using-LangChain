import langchain

print(langchain.__version__)


import streamlit as st

st.title("My First Streamlit App")

st.write("Hello, World!")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}! 👋")
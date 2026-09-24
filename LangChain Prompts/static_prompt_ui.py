## ==  This program is for to create UI and static prompts  == ##

from langchain_ollama import ChatOllama
from dotenv import  load_dotenv
import streamlit as st

load_dotenv()


model = ChatOllama(
    model="llama3",
    temperature=0.5
)

st.header('Research Tool')
user_input= st.text_input("Enter your prompt ")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)
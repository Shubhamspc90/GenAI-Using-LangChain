import streamlit as st
from langchain_ollama import ChatOllama

st.title("Shubham Ollama Chatbot")

llm = ChatOllama(
    model="llama3",
    temperature=0
)

question = st.text_input("Ask something:")

if question:
    result = llm.invoke(question)

    st.write(result.content)
    
# '''   
# to run:  streamlit run "LangChain Prompts/ollama_app.py"  
# syntax:  streamlit run "folder_name/file_name.py"                                    
#     ┌─────────────────────────────────────┐
#     │          Ollama Chatbot             │
#     │                                     │
#     │ Ask something:                      │
#     │ ┌─────────────────────────────────┐ │
#     │ │ What is the capital of India?   │ │
#     │ └─────────────────────────────────┘ │
#     │                                     │
#     │ New Delhi                           │
#     └─────────────────────────────────────┘

# The overall architecture

#              Streamlit UI
#                   ↓
#         User enters question
#                   ↓
#             LangChain
#                   ↓
#              ChatOllama
#                   ↓
#               Ollama
#                   ↓
#              Llama 3
#                   ↓
#              AI Response
#                   ↓
#            Streamlit UI

# '''
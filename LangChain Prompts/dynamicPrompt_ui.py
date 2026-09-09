from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import load_prompt

# -----------------------------
# Ollama Model
# -----------------------------
model = ChatOllama(
    model="llama3",
    temperature=0
)

# -----------------------------
# Streamlit UI
# -----------------------------
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# -----------------------------
# Load Prompt Template
# -----------------------------
template = load_prompt("LangChain Prompts/template.json")
# -----------------------------
# Summarize Button
# -----------------------------
if st.button("Summarize"):

    chain = template | model

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.write(result.content)
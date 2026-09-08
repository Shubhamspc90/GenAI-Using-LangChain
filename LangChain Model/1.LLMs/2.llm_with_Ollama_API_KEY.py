
### this is LLM version but currently   now it does not work with OpenAI with  Ollama API key ,,
# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# llm = OpenAI(
#     model="gpt-oss:20b",
#     api_key=os.getenv("OLLAMA_API_KEY"),
#     base_url="https://ollama.com/v1",
#     temperature=0
# )

# result = llm.invoke("What is the capital of India?")

# print(result)


# Solution :  API key + Ollama Cloud + Chat Model

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-oss:20b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
    temperature=0
)

result = llm.invoke("What is the Capital of INDIA??")

print(result.content)

# flow:
    
# Your Python Code
#       ↓
# LangChain ChatOpenAI
#       ↓
# OLLAMA_API_KEY 🔑
#       ↓
# https://ollama.com/v1
#       ↓
# Ollama Cloud ☁️
#       ↓
# gpt-oss:20b
#       ↓
# Answer


# Answer:  The capital of India is **New Delhi**.

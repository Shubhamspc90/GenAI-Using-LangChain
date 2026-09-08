#  #  for OPEN AI  , this code is for API key

# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = OpenAI(model="gpt-3.5-turbo-instruct")
# result = llm.invoke("what is the capital of INDIA ?")

# print(result)


# ================================Without API KEY======================

# #  for Ollama  locally 
# from langchain_ollama import ChatOllama
# from dotenv import load_dotenv
# llm = ChatOllama(
#     model="llama3",
#     temperature=0
# )

# result = llm.invoke("What is the capital of India?")

# print(result.content)




from langchain_ollama import OllamaLLM

# Local Ollama model initialize karein
llm = OllamaLLM(model="llama3")

# Prompt run karein
response = llm.invoke("Explain Quantum Computing in 2 sentences.")
print(response)
 
 
 
 
 


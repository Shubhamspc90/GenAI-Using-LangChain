from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3",
    temperature=0
)

result = model.invoke("What is the capital of India?")

print(result.content)


# code == Flow ==

# Your Python Program
#        ↓
# ChatOllama
#        ↓
# Ollama Server
#        ↓
# llama3 Model
#        ↓
# Model generates response
#        ↓
# LangChain AIMessage
#        ↓
# result.content
#        ↓
# Print answer



# this is the important concept. In your code, you are using an API, but you are not explicitly writing the API URL or API key.

# Without LangChain, you could communicate with Ollama's API yourself:

# Python
#   ↓
# HTTP Request
#   ↓
# http://localhost:11434/api/chat
#   ↓
# Ollama
#   ↓
# llama3

# With LangChain:

# Python
#   ↓
# ChatOllama
#   ↓
# HTTP Request
#   ↓
# Ollama API
#   ↓
# llama3
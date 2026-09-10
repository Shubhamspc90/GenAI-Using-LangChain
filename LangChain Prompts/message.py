from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama( model= 'llama3' ,temperature=0)

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about your self")
]

result = model.invoke(message)
message.append(AIMessage(result.content))

print(message)


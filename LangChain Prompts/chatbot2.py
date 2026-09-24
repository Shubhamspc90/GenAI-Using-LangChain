
# In this Chatbot you can see the message ,and which message belong to whome also.

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="llama3"
)

chat_history =[
    SystemMessage(content="Your are a helpful Ai Assistant")
]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
    
print(chat_history)
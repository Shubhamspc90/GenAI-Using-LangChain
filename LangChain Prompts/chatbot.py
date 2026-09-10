#  creteing Chatbot

from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
    model="llama3"
)

chat_history =[]
while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)
    
print(chat_history)


## after chating with our chat bot  ,below give is out history , but there is small problem ,there is no label like which message is of whome , so in chatbot2  i will solve this problem with the help of (MESSAGE)
#['hi', "Hi! It's nice to meet you. Is there something I can help you with or would you like to chat?", '2+3', "Nice to meetyou too!\n\nIt seems like you're already ready to get started with a fun conversation! I'm happy to chat with you, but I'llalso keep an eye out for any specific questions or topics you'd like to discuss.\n\nAs for the math problem, the answer to 2+3 is... (drumroll please)... 5!\n\nNow, what would you like to talk about?", 'exit']


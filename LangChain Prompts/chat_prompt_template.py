#ChatPromptTemplate is a reusable template for creating structured messages for chat models, with support for dynamic variables and different message roles.
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Explain in simple words, what is the {topic}")
])

prompt = chat_template.invoke({
    'domain': 'Cricket',
    'topic': 'No Ball'
})

print(prompt)
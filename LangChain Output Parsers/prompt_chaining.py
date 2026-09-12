from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOllama(
    model="llama3",
    temperature = 0
) 

# 1st Prompt
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd Prompt
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"]
)

# First prompt
prompt1 = template1.invoke({
    "topic": "black hole"
})

# Send first prompt to model
result1 = model.invoke(prompt1)

print("FIRST RESULT:")
print(result1.content)


# Second prompt
prompt2 = template2.invoke({
    "text": result1.content
})

# Send second prompt to model
result2 = model.invoke(prompt2)

print("\nSUMMARY:")
print(result2.content)


# What your code is doing
#        Topic: "black hole"
#               ↓
#        template1
#               ↓
#        LLM (Llama3)
#               ↓
#        Detailed report
#               ↓
#        template2
#               ↓
#        LLM (Llama3)
#               ↓
#        5-line summary
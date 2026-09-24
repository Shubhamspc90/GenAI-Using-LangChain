from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

model = ChatOllama(
    model="llama3",
    temperature=0
)

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple words."
)

final_prompt = prompt.invoke({
    "topic": "Machine Learning"
})

result = model.invoke(final_prompt)

print(result.content)

# FLOW

# User Input
#     ↓
# Prompt Template
#     ↓
# "Explain {topic} in simple words."
#     ↓
# topic = Machine Learning
#     ↓
# "Explain Machine Learning in simple words."
#     ↓
# LLM
#     ↓
# Response

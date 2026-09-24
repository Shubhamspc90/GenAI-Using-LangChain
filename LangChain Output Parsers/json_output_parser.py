from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatOllama(
    model="llama3",
    temperature= 0
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me  the  name,age and city of fictional person\n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template|model|parser

result = chain.invoke({})

print(result,"\n")
print(type(result))


# # OUTPUT

# {'name': 'Evelyn Stone', 'age': 32, 'city': 'Portland'} 

# <class 'dict'>

## ======  Complete Flow  ======##


#         PromptTemplate
#              │
#              │
#              ▼
#   "Give me name, age,
#    city of fictional person"
#              │
#              ▼
#     + format instructions
#              │
#              ▼
#          ChatOllama
#              │
#              ▼
#           Llama3
#              │
#              ▼
#    JSON response
#              │
#              ▼
#     JsonOutputParser
#              │
#              ▼
#      Python Dictionary
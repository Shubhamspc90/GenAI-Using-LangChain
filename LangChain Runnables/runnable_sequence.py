from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
import os
load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={
        "headers": {
            "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
        }
    },
    temperature=0
)

prompt1 = PromptTemplate(
    template= "write a joke about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template= "summarise the joke about {text}",
    input_variables=["text"]
)
parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser|prompt2,model,parser)

print(chain.invoke({'topic':'AI'}))

# output 

# The joke riffs on AI jargon: it says the AI needed therapy because it was “over‑thinking” its **neural network** and couldn’t stop **processing** its feelings—turning technical terms into a playful metaphor for anxiety.










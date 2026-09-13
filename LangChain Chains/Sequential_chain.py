from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOllama(
    model="llama3",
    temperature=0.5
)

prompt1 =PromptTemplate(
    template="Genereate a summary on this {topic} ",
    input_variables=["topic"]
)

prompt2 =PromptTemplate(
    template="generate the 5 line small summary from the {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1| model|parser|prompt2|model|parser

result = chain.invoke({'topic':'Amazon Forest'})
print("==============  Result  ==================\n")
print(result)






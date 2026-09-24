from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
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
prompt = PromptTemplate(
    template='Write the summary for the following {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader( "LangChain document loader/cricket.txt", encoding="utf-8")

doc = loader.load()

print(type(doc))
print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)


chain = prompt|model|parser

print(chain.invoke(doc[0].page_content))
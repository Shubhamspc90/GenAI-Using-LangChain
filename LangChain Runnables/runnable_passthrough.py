from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
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
prompt1 = PromptTemplate(
    template="create a joke on this {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="create the summy on this {text}",
    input_variables=['text']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1|model|parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'Summary':RunnableSequence(prompt2|model|parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})

print(result)
from langchain_community.document_loaders import CSVLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# -----------------------------
# 1. Load CSV file
# -----------------------------
loader = CSVLoader(
    file_path="LangChain Document Loader/Social_Network_Ads.csv"
)

data = loader.load()

print("Number of documents:", len(data))
print("\nFirst document:")
print(data[0])


# -----------------------------
# 2. Ollama Cloud LLM
# -----------------------------
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


# -----------------------------
# 3. Prompt
# -----------------------------
prompt = PromptTemplate(
    template="""
You are given data from a CSV file.

CSV DATA:
{data}

Answer the user's question using the CSV data.

Question:
{question}
""",
    input_variables=["data", "question"]
)


# -----------------------------
# 4. Output parser
# -----------------------------
parser = StrOutputParser()


# -----------------------------
# 5. Chain
# -----------------------------
chain = prompt | model | parser


# -----------------------------
# 6. Ask a question
# -----------------------------
question = "What is the age and estimated salary of the first person?"

# Convert ALL CSV documents into one text
csv_data = "\n".join(
    doc.page_content for doc in data
)

result = chain.invoke({
    "data": csv_data,
    "question": question
})

print("\nAnswer:")
print(result)
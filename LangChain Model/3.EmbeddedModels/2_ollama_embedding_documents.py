from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OllamaEmbeddings(
    model="mxbai-embed-large",
    dimensions=32
)

document = [
    "India is a Country",
    "China is a Country",
    "Nepal is a Country"
]
result = embedding.embed_documents(document)

print(str(result))
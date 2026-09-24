from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OllamaEmbeddings(
    model="mxbai-embed-large",dimensions=32
)

result = embedding.embed_query("Delhi is the capital of India")

print(str(result))
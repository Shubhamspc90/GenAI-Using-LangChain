from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings( model_name='sentence-transformers/all-MiniLM-L6-v2')


# # for single sentence
# text = "New Delhi is Capital of India"
# vector = embedding.embed_query(text)
# print(str(vector))


# for paragraph 
document = [
    "India is a Country",
    "China is a Country",
    "Nepal is a Country"
]
result = embedding.embed_documents(document)
print(str(result))








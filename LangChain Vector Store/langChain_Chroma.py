from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load .env
load_dotenv()


# --------------------------------------------------
# 1. Embedding Model
# --------------------------------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 2. Documents
# --------------------------------------------------
docs = [
    Document(
        page_content="Virat Kohli is an Indian cricketer and former captain of the Indian national cricket team.",
        metadata={"team": "RCB"}
    ),

    Document(
        page_content="Rohit Sharma is an Indian cricketer and former captain of the Indian national cricket team.",
        metadata={"team": "MI"}
    ),

    Document(
        page_content="MS Dhoni is an Indian cricketer and former captain of the Indian national cricket team.",
        metadata={"team": "CSK"}
    ),

    Document(
        page_content="Jasprit Bumrah is an Indian fast bowler known for his accuracy and death bowling.",
        metadata={"team": "MI"}
    ),

    Document(
        page_content="Ravindra Jadeja is an Indian all-rounder known for his batting, bowling and fielding.",
        metadata={"team": "CSK"}
    )
]


# --------------------------------------------------
# 3. Create Chroma Vector Store
# --------------------------------------------------
vector_store = Chroma(
    collection_name="sample",
    embedding_function=embeddings,
    persist_directory="./my_chroma_db"
)


# --------------------------------------------------
# 4. Add Documents
# --------------------------------------------------
ids = vector_store.add_documents(docs)

print("\nDocument IDs:")
print(ids)


# --------------------------------------------------
# 5. Get All Documents
# --------------------------------------------------
print("\nAll Documents:")

data = vector_store.get()

print(data)


# --------------------------------------------------
# 6. Similarity Search
# --------------------------------------------------
print("\nSimilarity Search:")

results = vector_store.similarity_search(
    "Who is the captain of RCB?",
    k=2
)

for doc in results:
    print("\nContent:", doc.page_content)
    print("Metadata:", doc.metadata)


# --------------------------------------------------
# 7. Similarity Search With Score
# --------------------------------------------------
print("\nSimilarity Search With Score:")

results_with_score = vector_store.similarity_search_with_score(
    "Indian fast bowler",
    k=2
)

for doc, score in results_with_score:
    print("\nContent:", doc.page_content)
    print("Score:", score)
    print("Metadata:", doc.metadata)


# --------------------------------------------------
# 8. Metadata Filter
# --------------------------------------------------
print("\nMetadata Filter - MI:")

results = vector_store.similarity_search(
    "Indian cricketer",
    k=2,
    filter={"team": "MI"}
)

for doc in results:
    print("\nContent:", doc.page_content)
    print("Metadata:", doc.metadata)


# --------------------------------------------------
# 9. Update Document
# --------------------------------------------------
print("\nUpdating first document...")

updated_doc = Document(
    page_content="Virat Kohli is an Indian cricketer, former captain of India, and a former RCB captain.",
    metadata={"team": "RCB"}
)

vector_store.update_documents(
    ids=[ids[0]],
    documents=[updated_doc]
)

print("Document updated successfully.")


# --------------------------------------------------
# 10. Verify Updated Document
# --------------------------------------------------
updated_results = vector_store.similarity_search(
    "Virat Kohli",
    k=1
)

print("\nUpdated Document:")

for doc in updated_results:
    print(doc.page_content)
    print(doc.metadata)


# --------------------------------------------------
# 11. Delete Document
# --------------------------------------------------
print("\nDeleting first document...")

vector_store.delete(ids=[ids[0]])

print("Document deleted successfully.")


# --------------------------------------------------
# 12. Check Remaining Documents
# --------------------------------------------------
print("\nRemaining Documents:")

data = vector_store.get()

print(data)
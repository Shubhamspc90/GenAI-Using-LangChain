
# ========= Not Working ==============#
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task='text-generation'
# )
# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India?")
# print(result.content)

# ========= Not Working ==============#

# import os
# from dotenv import load_dotenv
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen3-0.6B",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of India?")

# print(result.content)


# ========= Not Working ==============#

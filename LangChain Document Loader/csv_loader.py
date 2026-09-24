from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path='LangChain Document Loader/Social_Network_Ads.csv'
)

data = loader.load()

print(len(data))
print(data[0])
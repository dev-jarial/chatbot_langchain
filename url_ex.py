from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.redditinc.com/")
docs = loader.load()
print(docs[0].page_content)
# print(docs[0].page_content[0:500])

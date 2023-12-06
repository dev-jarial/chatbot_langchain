from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("GoogleCheatSheet.pdf")
pages = loader.load()

len(pages)
# print(pages)
page = pages[0]
# print(page.page_content[0:500])
print(page.page_content)
# print(page.metadata)

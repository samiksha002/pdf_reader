import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain import VectorDBQA, OpenAI


'''import pinecone
pinecone.init(api_key="ff064aa0-2aba-489e-8a14-47a6dfde1d6a", environment="us-west1-gcp-free")'''
# print("HELLO VECTOR STORE")
# file_name = r'C:\\Users\\DELL\\intro-to-vector-db\\mediumlogs\\mediumlog1.txt'
#
# with open(file_name, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
#     print(lines)
# loader = TextLoader(r"C:\Users\DELL\OneDrive\Desktop\mediumblog.txt")
# document = loader.load()
# print(document)
loader=TextLoader("C://Users//DELL//intro-to-vector-db//mediumlogs//mediumlog1.txt",encoding="UTF-8"
    )
document = loader.load()
print(document)
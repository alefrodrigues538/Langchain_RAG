import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag.config import DATA_PATH

def load_and_split_documents():
    documents = []
    for filename in os.listdir(DATA_PATH):
        if filename.endswith((".txt", ".md")):
            loader = TextLoader(os.path.join(DATA_PATH, filename))
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

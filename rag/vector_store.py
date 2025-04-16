from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from rag.config import COHERE_API_KEY, INDEX_PATH
from rag.document_loader import load_and_split_documents

def create_vector_store():
    documents = load_and_split_documents()
    embeddings = CohereEmbeddings(model="embed-english-light-v2.0", cohere_api_key=COHERE_API_KEY)
    vector_store = Chroma.from_documents(documents, embeddings, persist_directory=INDEX_PATH)
    vector_store.persist()

def load_vector_store():
    embeddings = CohereEmbeddings(model="embed-english-light-v2.0", cohere_api_key=COHERE_API_KEY)
    return Chroma(persist_directory=INDEX_PATH, embedding_function=embeddings)

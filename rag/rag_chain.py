from langchain_cohere import ChatCohere
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from rag.config import COHERE_API_KEY
from rag.vector_store import load_vector_store

def build_rag_chain():
    llm = ChatCohere(cohere_api_key=COHERE_API_KEY, model="command-r")
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory, verbose=True)

from langchain_cohere import ChatCohere
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from rag.config import COHERE_API_KEY
from rag.vector_store import load_vector_store

def build_rag_chain():
    # Inicializa o modelo de linguagem da Cohere
    llm = ChatCohere(cohere_api_key=COHERE_API_KEY, model="command-r")

    # Carrega o vetorstore com os documentos fornecidos
    vector_store = load_vector_store()

    # Cria o retriever a partir do vetorstore
    retriever = vector_store.as_retriever()

    # Configura a memória da conversa
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    # Cria o pipeline RAG com o modelo, retriever e memória
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

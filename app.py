import streamlit as st
from rag.rag_chain import build_rag_chain

st.set_page_config(page_title="Chatbot RAG com Cohere", layout="wide")
st.title("🤖 Chatbot RAG com Cohere")

# Inicialize o chain e o histórico de mensagens
if "chain" not in st.session_state:
    st.session_state.chain = build_rag_chain()
    st.session_state.messages = []

# Exibe o histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada para nova pergunta
if prompt := st.chat_input("Digite sua pergunta aqui..."):
    # Adiciona a pergunta ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Exibe o spinner enquanto processa a resposta
    with st.chat_message("assistant"):
        with st.spinner("Gerando resposta..."):
            response = st.session_state.chain.run(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

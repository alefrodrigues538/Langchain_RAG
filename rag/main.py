from rag.vector_store import create_vector_store
from rag.rag_chain import build_rag_chain

def main():
    print("🚀 Inicializando o sistema RAG... Por favor, aguarde!")
    create_vector_store()
    rag_chain = build_rag_chain()
    print("✅ Sistema RAG pronto! 🎉")
    print("💡 Digite sua pergunta abaixo ou 'sair' para encerrar o programa.")

    while True:
        query = input("❓ Pergunta: ")
        if query.lower() == "sair":
            print("👋 Encerrando o sistema. Até a próxima!")
            break
        answer = rag_chain.run(query)
        print(f"📝 Resposta: {answer}\n")

if __name__ == "__main__":
    main()
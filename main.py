from ai.gemini import criar_cliente , criar_chat , enviar_mensagem , linha



def iniciar_sistema():
    try:
        client = criar_cliente()
        chat = criar_chat(client)
        
        print("=" * 35)
        print("\tCITIZEN ASSIST AI")
        print("=" * 35)
        print("Assistente iniciado!")
        print("Digite 'sair' para encerrar.\n")
        return client , chat
        
    except Exception as erro:
        print(f"Erro ao iniciar o sistema: {erro}")
        return None , None


def iniciar_conversa(chat):
    while True:
        try:
            pergunta = linha("Você: ")
        except KeyboardInterrupt:
            print("\nEncerrando Citizen Assist AI...")
            break
        
        if pergunta.lower() in ["sair", "s"]:
            print("\nEncerrando Citizen Assist AI...")
            break
        
        if not pergunta:
            print("\nDigite uma mensagem para continuar")
            continue
        
        try:
            resposta = enviar_mensagem(chat , pergunta)
            if resposta:
                print(f"\nCitizen Assist AI: {resposta}\n")
            else:
                print("\nNão foi possível gerar uma resposta\n")
        except KeyboardInterrupt:
            print("\nEncerrando Citizen Assist AI...")
            break
        except Exception as erro:
            print(f"ERRO de resposta da API: {erro}")
            print("Porfavor tente novamente")



def main():
    client , chat = iniciar_sistema()
    
    if chat:
        iniciar_conversa(chat)


if __name__ == "__main__":
    main()

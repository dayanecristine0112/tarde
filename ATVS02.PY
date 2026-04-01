def sugerir_atividade():
    # Pergunta ao usuário como ele se sente
    # .strip() remove espaços extras, .lower() converte para minúsculas para facilitar a comparação
    sentimento = input("Olá! Como você está se sentindo hoje? (feliz, cansado, estressado, animado): ").strip().lower()

    print("\n--- Sugestão do Dia ---")

    # Estrutura condicional para analisar a resposta
    if sentimento in ["feliz", "animado"]:
        print(f"Que ótimo que você está {sentimento}! 🎉")
        print("Sugestão: Que tal ligar para um amigo, ir a um evento social ou adiantar aquele projeto importante?")
    
    elif sentimento == "cansado":
        print("Entendi... parece que o corpo precisa de um tempo. 😴")
        print("Sugestão: Tire uma soneca, assista a um filme leve ou vá dormir mais cedo hoje.")
    
    elif sentimento == "estressado":
        print("Sinto muito que você esteja estressado(a). Respire fundo... 🧘‍♂️")
        print("Sugestão: Faça uma caminhada leve, pratique meditação, ou ouça músicas relaxantes.")
    
    else:
        # Resposta padrão caso o sentimento não esteja mapeado
        print("Entendi como você está. 😊")
        print("Sugestão: Faça uma pausa, tome uma água e respire fundo antes de continuar.")

# Executa o programa
if __name__ == "__main__":
    sugerir_atividade()

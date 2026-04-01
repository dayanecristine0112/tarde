def sistema_acesso_abrigo():
    print("--- Sistema de Acesso: Abrigo Pós-Apocalíptico ---")

    try:
        # Entrada de dados
        energia = int(input("Informe o nível de energia (0 a 100): "))
        item_especial = input("Possui item especial? (sim/nao): ").lower().strip()

        # Validação de energia
        if energia < 0 or energia > 100:
            print("❌ Erro: O nível de energia deve ser entre 0 e 100.")
            return

        # Validação do item especial
        if item_especial not in ['sim', 'nao']:
            print("❌ Erro: Resposta de item especial inválida. Responda apenas 'sim' ou 'nao'.")
            return

        # Lógica de decisão
        pode_entrar = False
        mensagem = ""

        if energia < 30:
            pode_entrar = False
            mensagem = "⚠️ Acesso negado: Nível de energia muito baixo. O personagem não consegue passar da porta."
        elif 30 <= energia <= 70:
            if item_especial == 'sim':
                pode_entrar = True
                mensagem = "✅ Acesso condicional: Energia média, mas o item especial permitiu a entrada."
            else:
                pode_entrar = False
                mensagem = "⚠️ Acesso negado: Energia média e sem item especial."
        else: # energia > 70
            pode_entrar = True
            mensagem = "✅ Acesso liberado: Energia alta, entrada garantida."

        # Exibição do resultado
        print("-" * 40)
        print("RESULTADO:", mensagem)
        print("-" * 40)

    except ValueError:
        print("❌ Erro: Por favor, insira um número inteiro válido para a energia.")

# Executar o programa
sistema_acesso_abrigo()

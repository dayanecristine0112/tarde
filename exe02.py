senha = input("Digite sua senha para avaliação: ")

# Regras de tamanho
tamanho = len(senha)
if tamanho < 6:
    nivel = "Fraca"
elif 6 <= tamanho <= 8:
    nivel = "Média"
else:
    nivel = "Forte"

# Verificação de segurança adicional
apenas_numeros = senha.isdigit()
alerta = ""
if apenas_numeros:
    alerta = "⚠️ ALERTA: Sua senha contém apenas números e é pouco segura, independente do tamanho."

# Sugestões de melhoria
sugestoes = []
if tamanho <= 8:
    sugestoes.append("- Aumente o número de caracteres para mais de 8.")
if apenas_numeros:
    sugestoes.append("- Misture letras (maiúsculas e minúsculas) e símbolos (ex: @, #, $).")
if not apenas_numeros and not any(c.isdigit() for c in senha):
    sugestoes.append("- Adicione alguns números à sua senha.")

# Exibição do resultado
print(f"\nNível da senha: {nivel}")
if alerta:
    print(alerta)

if sugestoes:
    print("\nComo melhorar sua segurança:")
    for s in sugestoes:
        print(s)
else:
    print("\nParabéns! Sua senha segue boas práticas de segurança.")

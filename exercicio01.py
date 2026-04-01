# 1. Variável 'cidade' (texto)
cidade = input("Digite o nome da sua cidade: ")

# 2. Variável 'ano' (texto, pois não faremos contas com ele, ou int para número)
ano = input("Digite o ano atual: ")

# 3. Variável 'temperatura' (float para aceitar números decimais)
temperatura = float(input("Digite a temperatura média da sua cidade (°C): "))

# Exibindo os resultados para confirmar
print("\n--- Dados Recebidos ---")
print(f"Cidade: {cidade}")
print(f"Ano: {ano}")
print(f"Temperatura: {temperatura}°C")

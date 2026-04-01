# 1. Pedindo os números ao usuário
# Usamos float() para permitir números decimais (ex: 2.5)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Realizando as operações matemáticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# 3. Exibindo os resultados
print("\n--- Resultados ---")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")

# Tratamento para divisão por zero
if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {num1} / {num2} = {divisao}")
else:
    print("Divisão: Não é possível dividir por zero.")

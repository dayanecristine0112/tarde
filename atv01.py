# Cria uma lista vazia para armazenar os 5 números
vetor = []

# Laço para ler 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num) # Armazena o número no vetor

# Mostra os números armazenados
print("\nOs números digitados foram:")
print(vetor)







# Inicializa uma lista vazia
numeros = []

# Lê 10 números reais
print("Digite 10 números reais:")
for i in range(10):
    num = float(input(f"{i+1}º número: "))
    numeros.append(num)

# Mostra na ordem inversa
print("\nNúmeros na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])









# Criando uma lista para armazenar as notas
notas = []

# Lendo as 4 notas
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Calculando a média
media = sum(notas) / len(notas)

# Mostrando os resultados
print(f"\nNotas digitadas: {notas}")
print(f"Média final: {media:.2f}")

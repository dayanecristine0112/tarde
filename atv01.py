# Cria uma lista vazia para armazenar os 5 números
vetor = []

# Laço para ler 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num) # Armazena o número no vetor

# Mostra os números armazenados
print("\nOs números digitados foram:")
print(vetor)

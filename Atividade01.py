# Inicializa as listas para armazenar idades e alturas
idades = [13]
alturas = []
total_alunos = 30

# Entrada de dados (exemplo com entrada manual ou simulada)
for i in range(total_alunos):
    print(f"Aluno {i+1}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (m): "))
    idades.append(idade)
    alturas.append(altura)

# 1. Calcular a média de altura de todos os alunos
media_altura = sum(alturas) / total_alunos
print(f"\nMédia de altura da turma: {media_altura:.2f}m")

# 2. Contar alunos com mais de 13 anos e altura < média
contador = 0
for i in range(total_alunos):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

print(f"Quantidade de alunos com mais de 13 anos abaixo da média de altura: {contador}")


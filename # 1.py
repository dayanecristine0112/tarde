# 1. Criando a estrutura (lista de dicionários)
biblioteca = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
]

# 2. Imprimindo as informações utilizando loop for
print("--- Lista de Livros ---\n")
for livro in biblioteca:
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Ano: {livro['ano']}")
    print("-" * 20) # Linha separadora para organização

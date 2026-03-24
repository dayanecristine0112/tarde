idade = int(input("Digite sua idade: "))


if idade >= 18:
    print(F"Você é adulto. idade de {idade}")
elif idade >= 12:
    print(F"Você é adolescente. idade de {idade}")
else:
    print(F"Você é uma criança. idade de {idade}")
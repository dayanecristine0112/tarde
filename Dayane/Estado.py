estado = input("Digite o estado civil (Casado, Solteio, Divorciado, Viuvo, Outros ): ").upper()

if estado == "C":
    print("voce e  - Casado")
elif estado == "S":
    print("voce e Solteiro - Solteiro")
elif estado == "D":
    print("voce e Divorciado  - Divorciado")
elif estado == "V":
    print("Voce e  - Viúvo")
elif estado == "voce e outros":
    print("O - Outros")
else:
    print("Opção inválida.")
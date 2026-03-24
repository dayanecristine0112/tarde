nota1= float(input("Digite a nota 1:"))
nota2= float(input("Digite a nota 2 :"))
nota3 = float(input("Digite a nota 3:"))
nota4 = float(input("Digite a nota 4 :"))
media=(nota1+nota2+nota3+nota4)/4

print(f"a nota media é {media:.1f}")

if media >= 7:
    print('voce está aprovado')
elif media >= 5:
    print('voce esta em recuperacao')
else: 
    print('voce está reprovado')


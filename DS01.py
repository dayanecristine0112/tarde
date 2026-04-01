# Entrada de dados
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

# Definição de preços
preco_gasolina = 5.50
preco_alcool = 3.89

# Lógica de cálculo
if tipo == 'A':
    preco_total = litros * preco_alcool
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    valor_final = preco_total * (1 - desconto)

elif tipo == 'G':
    preco_total = litros * preco_gasolina
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    valor_final = preco_total * (1 - desconto)

else:
    valor_final = None
    print("Tipo de combustível inválido!")

# Saída do resultado
if valor_final is not None:
    print(f"Valor a ser pago: R$ {valor_final:.2f}")








#Algoritmo PostoCombustivel
#Var
    #litros, precoLitro, total : Real
    #tipo : Caractere
#Inicio
    #// Entrada de dados
    #Leia(litros)
    #Escreva("Digite o tipo de combustível (A-álcool, G-gasolina): ")
    #Leia(tipo)

    #// Definição de preços
    #Se (tipo = "A") ou (tipo = "a") Entao
        #precoLitro <- 3.89
    #SenNao
       # Se (tipo = "G") ou (tipo = "g") Entao
        #    precoLitro <- 5.50
       # Senao
        #    Escreva("Tipo de combustível inválido!")
            #FimAlgoritmo // Encerra se o tipo for inválido
       # FimSe
   # FimSe#

    #// Cálculo
    #total <- litros * precoLitro

    #// Saída
   # Escreva("Valor total a pagar: R$ ", total:0:2)
#FimAlgoritmo

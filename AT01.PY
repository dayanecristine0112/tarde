

quantidade = int(input("Quantos termos da sequência Fibonacci você deseja ver? "))

a = 0
b = 1

for i in range(quantidade):
    print(a, end=" ")
    a, b = b, a + b


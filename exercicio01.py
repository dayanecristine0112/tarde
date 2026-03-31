numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Os números digitados foram:")
for n in numeros:
    print(n) 
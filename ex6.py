total = 0

tam = int(input("Digite a quantidade de numeros de entrada: "))

while tam>0:
    number = int(input("Digite um numero: "))
    total=number + total
    tam-=1

print(f"Total: {total}")


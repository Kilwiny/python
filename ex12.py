
lista =[]

tam = int(input("Digite a quantidade de termos: "))

for i in range(tam):
    num = int(input("Digite um número: "))
    lista.append(num)


for i in lista:
    if i == 1 or i % 2 !=0: print(i)
tam = int(input("Digite a quantidade de numeros: "))
lista =[]
for i in range(tam):
    num = int(input("Digite um número: "))
    lista.append(num)

lista.sort()

print(f"O maior numero da lista é: {lista[tam-1]}")
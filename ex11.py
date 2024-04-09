lista =[]
tam = int(input("Digite a quantidade de usuarios: "))

for i in range(tam):
    nome = input("Digite um nome: ")
    lista.append(nome)


print(lista)

for i in range(1, tam, 2):
    print(lista[i])
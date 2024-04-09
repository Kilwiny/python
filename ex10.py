import functools
lista = []

tam = int(input("Digite quantos numeros quer imprimir: "))

for i in range(tam):
    number = int(input("Digite um numero: "))
    lista.append(number)
    

media =functools.reduce(lambda a, b: a+b, lista)/tam

print(f"A media desses numeros é: {media}")


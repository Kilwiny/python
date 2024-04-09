palavras =[]

tam = int(input("Quantas palavras quer digitar: "))

for i in range(tam):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)


temp = palavras[0]
for p in palavras:
    if len(palavra) < len(p):
        palavra = p

print(f"A maior palavra é {palavra}")
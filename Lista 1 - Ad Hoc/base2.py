lista = [int(x) for x in input().split()]

soma = 0
for i in range(0, len(lista)):
    if lista[i] != 0:
        soma += lista[i]*pow(2, i)

print(soma)
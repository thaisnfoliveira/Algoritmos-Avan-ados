n = int(input())
names = set()
repetidos = []

for i in range(n):
    lista = input().split()
    nome = "".join([palavra[0].upper() for palavra in lista[1:]])
    if nome in names:
        names.remove(nome)
        repetidos.append(nome)
    if nome not in repetidos:
        names.add(nome)
print(len(names))
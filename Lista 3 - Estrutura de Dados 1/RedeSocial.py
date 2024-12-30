n, k = map(int, input().split())
ids = list(map(int, input().split()))

ordem = []
tela = set()
for i in ids:
    if i not in tela:
        if len(ordem)>k:
            removido = ordem.pop(0)
            tela.remove(removido)
        ordem.append(i)
        tela.add(i)

ordem.reverse()
print(len(ordem))
print(*ordem)
n, k = map(int, input().split())
jogadores = list(map(int, input().split()))
vitorias = 0
atual = jogadores[0]

for i in range(1, n):
    if atual>jogadores[i]:
        vitorias +=1
    else:
        atual = jogadores[i]
        vitorias = 1
    if vitorias == k:
        break

print(atual)
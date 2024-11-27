n, m = map(int, input().split())
if n>m:
    max_jogadas = m
else:
    max_jogadas = n
if max_jogadas %2 == 0:
    vencedor = "Malvika"
else:
    vencedor = "Akshat"
print(vencedor)
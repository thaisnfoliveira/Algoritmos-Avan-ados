t = int(input())
results = []

for i in range(t):
    s = input()
    pilha = []
    for c in s:
        if pilha and ((pilha[-1] == "A" and c == 'B') or (pilha[-1]=='B' and c == 'B')):
            pilha.pop()
        else:
            pilha.append(c)
    
    results.append(len(pilha))

print("\n".join(map(str, results)))
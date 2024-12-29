n = int(input())
conversas = []
amigos = set()

for i in range(n):
    msg = input()
    if msg not in amigos:
        conversas.append(msg)
        amigos.add(msg)
    else:
        conversas.remove(msg)
        conversas.append(msg)
conversas.reverse()
print("\n".join(conversas))
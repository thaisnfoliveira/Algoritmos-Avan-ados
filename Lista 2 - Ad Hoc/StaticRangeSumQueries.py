n, q = map(int, input().split())
input_numbers = [int(x) for x in input().split()]

#soma acumulada
soma_acum = [0]
for num in input_numbers:
    soma_acum.append(soma_acum[-1] + num)
    
for i in range(q):
    a, b = map(int, input().split())
    print(soma_acum[b] - soma_acum[a-1])
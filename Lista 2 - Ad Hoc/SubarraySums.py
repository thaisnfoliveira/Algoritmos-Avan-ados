n, x = map(int, input().split())
arr = [int(x) for x in input().split()]

left = 0 
soma_atual = 0 
contador = 0 

for right in range(n):
    soma_atual += arr[right]
    while soma_atual > x and left <= right:
        soma_atual -= arr[left]
        left += 1 

    if soma_atual == x:
        contador += 1 

print(contador)
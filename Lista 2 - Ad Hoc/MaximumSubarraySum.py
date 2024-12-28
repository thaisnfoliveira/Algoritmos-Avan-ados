n = int(input())
arr = [int(x) for x in input().split()]

max_atual = arr[0]
max_total = arr[0]

for i in range(1, n):
    max_atual = max(arr[i], max_atual + arr[i])
    max_total = max(max_total, max_atual)

print(max_total)
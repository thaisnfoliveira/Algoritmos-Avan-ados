a, b = map(int, input().split())

cont = 0

for num in range(a, b+1):
    num = str(num)
    if num[0] == num[-1]:
        if num == num[::-1]:
            cont += 1

print(cont)
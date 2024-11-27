n, q = map(int, input().split())
s = list(input().strip())

total_abc = 0
for i in range(n - 2):
    if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
        total_abc += 1

for _ in range(q):
    x, c = input().split()
    x = int(x) - 1 

    for i in range(x - 2, x + 1):
        if 0 <= i <= n - 3 and s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            total_abc -= 1

    s[x] = c

    for i in range(x - 2, x + 1):
        if 0 <= i <= n - 3 and s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            total_abc += 1

    print(total_abc)
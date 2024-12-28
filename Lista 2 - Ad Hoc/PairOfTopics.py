n = int(input())
professor = [int(x) for x in input().split()]
alunos = [int(x) for x in input().split()]

dif = [professor[i] - alunos[i] for i in range(n)]
dif.sort()
count = 0

left = 0
right = n-1

while left<right:
    if dif[left] + dif[right]>0:
        count += right - left
        right -=1
    else:
        left += 1

print(count)
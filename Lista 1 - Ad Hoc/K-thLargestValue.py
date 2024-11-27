n, q = map(int, input().split())
arr = [int(x) for x in input().split()]

cont1 = 0
for i in range(0, len(arr)):
    if arr[i] == 1:
        cont1+=1
        
for i in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if arr[k-1] == 0:
            arr[k-1] = 1
            cont1 += 1
        else:
            arr[k-1] = 0
            cont1 -= 1
    elif t == 2:
        if cont1>=k:
            print(1)
        else:
            print(0)
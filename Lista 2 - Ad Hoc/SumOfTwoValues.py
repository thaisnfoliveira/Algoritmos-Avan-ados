n, x = map(int, input().split())
arr = list(map(int, input().split()))

indexed_arr = [(arr[i], i + 1) for i in range(n)]
indexed_arr.sort()

left, right = 0, n - 1

while left < right:
    current_sum = indexed_arr[left][0] + indexed_arr[right][0]
    
    if current_sum == x:
        print(min(indexed_arr[left][1], indexed_arr[right][1]), 
              max(indexed_arr[left][1], indexed_arr[right][1]))
        break
    elif current_sum < x:
        left += 1 
    else:
        right -= 1 

else:
    print("IMPOSSIBLE")

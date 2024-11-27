n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
min_difference = float('inf')
window_size = n - k

for i in range(n - window_size+1):
    difference = arr[i+window_size-1]-arr[i]
    min_difference = min(min_difference, difference)
print(min_difference)
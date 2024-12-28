n = int(input())
musicas = list(map(int, input().split()))
m = 0
playlist = set()
left = 0

for i in range(n):
    while musicas[i] in playlist:
        playlist.remove(musicas[left])
        left += 1
    
    playlist.add(musicas[i])
    m = max(m, i -left +1)

print(m)
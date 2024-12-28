n = int(input()) 
chat_list = [] 
seen = set()

for i in range(n):
    friend = input().strip()
    if friend in seen:
        chat_list.remove(friend) 
    else:
        seen.add(friend) 
    chat_list.append(friend)


print("\n".join(reversed(chat_list)))

N = int(input())

title_dict = {}
for i in range(N):
    title = input()
    if title in title_dict:
        title_dict[title] += 1
    else:
        title_dict[title] = 1

max_num = max(title_dict.values())
answer = ''

for (k, v) in title_dict.items():
    if max_num == v:
        if answer:
            answer = answer if answer < k else k
        else:
            answer = k

print(answer)

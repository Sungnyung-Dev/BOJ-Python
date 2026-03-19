N = int(input())
cnt = 0

for i in range(N):
    Word = input()
    seen = list(Word[0])
    for j in range(1, len(Word)):
        if Word[j] == Word[j-1]:
            continue
        if Word[j] in seen:
            break
        seen.append(Word[j])
    else:
        cnt += 1

print(cnt)

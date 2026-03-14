N, M = map(int, input().split())

result = list()

for idx in range(N):
    result.append(0)

for idx in range(M):
    i, j, k = map(int, input().split())
    for idx2 in range(i - 1, j):
        result[idx2] = k

print(*result)
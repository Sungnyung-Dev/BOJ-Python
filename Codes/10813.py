N, M = map(int, input().split())

result = list()

for idx in range(N):
    result.append(idx + 1)

for idx in range(M):
    i, j = map(int, input().split())
    result[i - 1], result[j - 1] = result[j - 1], result[i - 1]
    
print(*result)
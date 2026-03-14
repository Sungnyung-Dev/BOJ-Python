N = int(input())
Score = list(map(int, input().split()))
M = max(Score)
result = 0

for i in range(N):
    result += Score[i]/M*100

print(result/N)
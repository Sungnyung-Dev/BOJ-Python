N = list(input())
isP = True

for i in range(len(N)//2):
    if (N[i] != N[len(N)-i-1]):
        isP = False
        break

print(int(isP))
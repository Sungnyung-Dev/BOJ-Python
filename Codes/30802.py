N = int(input())

TNin = input()
TN = list(map(int, TNin.split()))

T, P = map(int, input().split())

Tout = 0
for i in range(len(TN)):
    Tout += (TN[i] - 1) // T + 1

print(Tout)
print(N // P, N % P)

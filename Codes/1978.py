def isPM(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())

Nin = list(map(int, input().split()))

count = 0
for i in Nin:
    if i > 1 and isPM(i):
        count += 1
        
print(count)
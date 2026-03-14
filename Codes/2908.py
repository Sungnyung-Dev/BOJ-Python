A, B = map(list, input().split())

A.reverse()
B.reverse()

resA = 0
resB = 0

for i in range(3):
    resA += int(A[i])*10**(2-i)
    resB += int(B[i])*10**(2-i)
    
print(resA) if resA > resB else print(resB)
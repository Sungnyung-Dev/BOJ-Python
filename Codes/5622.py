Word = list(input())
arr = ['ABC', 'DEF', "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0

for i in range(len(Word)):
    for j in range(len(arr)):
        if Word[i] in arr[j]:
            result += j + 3
            
print(result)
N = int(input())

for i in range(N):
    print(' '*(N-i-1), end='')
    print('*'*((i+1)*2-1), end='')
    print()
for i in range(N-1, 0, -1):
    print(' '*(N-i), end='')
    print('*'*(i*2-1), end='')
    print()
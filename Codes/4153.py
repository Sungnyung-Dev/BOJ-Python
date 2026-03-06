inputList = []

while True:
    inputList.append(input())
    if inputList[-1] == '0 0 0':
        break
    
for i in range(len(inputList)-1):
    a, b, c = map(int, inputList[i].split())
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')

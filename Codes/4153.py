inputList = []
i = 0

while True:
    
    inputList.append(input())
    
    if inputList[-1] == '0 0 0':
        break
    
    a, b, c = map(int, inputList[i].split())
    
    sides = sorted([a, b, c])
    
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("right")
    else:
        print("wrong")
        
    i += 1
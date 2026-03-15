Word = input().upper()
Word_list = list(set(Word))
cnt = list()

for i in Word_list:
    cnt.append(Word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(Word_list[cnt.index(max(cnt))])
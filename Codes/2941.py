Word = input()

Croaita = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in Croaita:
    Word = Word.replace(i, "a")

print(len(Word))
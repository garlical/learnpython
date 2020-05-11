import re
hand = open('test.txt')

numlist = list()

for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) <= 0 : continue
    if len(x) == 1 :
        num = int(x[0])
    if len(x) > 1 : continue
    numlist.append(num)

print(numlist)
print(sum(numlist))

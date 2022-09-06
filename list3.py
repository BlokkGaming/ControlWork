i = 0

num = input('сколько строк будет в массиве? \n')

num = int(num)

l = []

while i != num:
    i += 1
    l.append(input('впишите строку №' + str(i) + ': \n'))

i = 0
k = []

while i != num:
    if len(l[i]) <= 3:
        k.append(l[i])
    i += 1

print(k)

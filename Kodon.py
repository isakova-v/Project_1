l = input()
L = []
k = ''
for i in range(len(l)):
    k += l[i]
    if i%3 == 2:
        L.append(k)
        k = ''

print(L)
import numpy as np
L = int(input())
h = int(input())
a = int(input())
t = int(input())
n = t*2

K = []
def X_Y(L, t, h, a):
    for i in range(t):
        x = (L / n) * i
        if i%2 == 0:
            y = 0
        else:
            y = h + (L/n)*np.sin(a*np.pi/180)
        k = (x, y)
        K.append(k)
    print(K)

X_Y(L, t, h, a)

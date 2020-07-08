import matplotlib.pyplot as plt
import numpy as np
import math

S = 1
N = 221
u = {}
b = 20


def gaussian(n):
    return math.e**(-(((n-60)/(5))**2))


def Sf(i):
    if i == 90:
        return 1.075
    else:
        return 1


x = []
for i in range(math.ceil(120/S)):
    x.append(gaussian(i))


for n in range(N):
    if n < 120/S:
        u[n, 0] = x[n]
    else:
        u[n, 0] = 0

for i in range(1, 220):
    u[0, i] = 0

for n in range(1, N):
    j = 1 if n < 75/S else 0
    for i in range(j, 220):
        if (i != 0 and i != 219):
            u[n, i] = (Sf(i)**2) * (u[n-1, i+1] - 2*u[n-1, i] +
                                u[n-1, i-1]) + 2*u[n-1, i]
        elif i == 0:
            u[n, i] = (Sf(i)**2) * (u[n-1, i+1] - 2*u[n-1, i]) + 2*u[n-1, i]
        else:
            u[n, i] = (Sf(i)**2) * (- 2*u[n-1, i] + u[n-1, i-1]) + 2*u[n-1, i]
        if n != 1:
            u[n, i] -= u[n-2, i]

u_plot = []
aux = []
aux2 = []
for i in range(70,110):
    aux.append(u[190,i])
    aux2.append(u[200,i])
u_plot.append(aux)
u_plot.append(aux2)
t1 = np.arange(70, 110, 1)

plt.figure()
plt.plot(t1, u_plot[0], 'k', label="n=190")
plt.plot(t1, u_plot[1], 'k:', label="n=200")
plt.ylim(-1,1)
plt.legend()


plt.show()

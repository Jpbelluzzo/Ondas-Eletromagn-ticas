import matplotlib.pyplot as plt
import numpy as np
import math

S = 1.0005
N = 221
u = {}
b = 20


def gaussian(n):
    return math.e**(-(((n-60)/(20))**2))


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
    j = 1 if n < 120/S else 0
    for i in range(j, 220):
        if (i != 0 and i != 219):
            u[n, i] = (S**2) * (u[n-1, i+1] - 2*u[n-1, i] +
                                u[n-1, i-1]) + 2*u[n-1, i]
        elif i == 0:
            u[n, i] = (S**2) * (u[n-1, i+1] - 2*u[n-1, i]) + 2*u[n-1, i]
        else:
            u[n, i] = (S**2) * (- 2*u[n-1, i] + u[n-1, i-1]) + 2*u[n-1, i]
        if n != 1:
            u[n, i] -= u[n-2, i]

u_plot = []

for n in range(200, 230, 10):
    aux = []
    for i in range(20):
        aux.append(u[n, i])
    u_plot.append(aux)

t1 = np.arange(0, 20, 1)

plt.figure()
plt.plot(t1, u_plot[0], 'k', label="n=200")
plt.plot(t1, u_plot[1], 'k:', label="n=210")
plt.plot(t1, u_plot[2], 'k--', label="n=220")
plt.legend()
plt.ylim(-0.04, 0.04)

plt.show()

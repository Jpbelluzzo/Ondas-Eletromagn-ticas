import matplotlib.pyplot as plt
import numpy as np
import math

S = 0.5
N = int(200/S)
u = {}
b = 20


def gaussian(n):
    return math.e**(-(((n-50/S)/(20/S))**2))


x = []
for i in range(math.ceil(100/S)):
    x.append(gaussian(i))

plt.plot(x)
plt.show()

for n in range(N):
    if n < 100/S:
        u[n, 0] = x[n]
    else:
        u[n, 0] = 0

for i in range(1, 200):
    u[0, i] = 0

for n in range(1, N):
    j = 1 if n < 100/S else 0
    for i in range(j, 200):
        if (i != 0 and i != 199):
            u[n, i] = (S**2) * (u[n-1, i+1] - 2*u[n-1, i] +
                                u[n-1, i-1]) + 2*u[n-1, i]
        elif i == 0:
            u[n, i] = (S**2) * (u[n-1, i+1] - 2*u[n-1, i]) + 2*u[n-1, i]
        else:
            u[n, i] = (S**2) * (- 2*u[n-1, i] + u[n-1, i-1]) + 2*u[n-1, i]
        if n != 1:
            u[n, i] -= u[n-2, i]

u_plot_S1 = []

for i in range(200):
    u_plot_S1.append(u[int(190/S), i])

t1 = np.arange(0, 200, 1)

plt.figure()
plt.plot(t1, u_plot_S1, 'k')

plt.show()

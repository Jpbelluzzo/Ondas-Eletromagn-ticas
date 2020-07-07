import matplotlib.pyplot as plt
import numpy as np
import math

N = int(200/0.775)
u = {}
b = 20


def gaussian(n):
    return math.e**(-(((n-50/S(n))/(20/S(n)))**2))


def S(n):
    if n < 140:
        return 1
    else:
        return 0.25


x = []
for i in range(math.ceil(100/0.775)):
    x.append(gaussian(i))
'''
plt.plot(x)
plt.show()
'''
for n in range(N):
    if n < 100/0.775:
        u[n, 0] = x[n]
    else:
        u[n, 0] = 0

for i in range(1, 200):
    u[0, i] = 0

for n in range(1, N):
    j = 1 if n < 100/0.775 else 0
    for i in range(j, 200):
        if (i != 0 and i != 199):
            u[n, i] = (S(i)**2) * (u[n-1, i+1] - 2*u[n-1, i] +
                                   u[n-1, i-1]) + 2*u[n-1, i]
        elif i == 0:
            u[n, i] = (S(i)**2) * (u[n-1, i+1] - 2*u[n-1, i]) + 2*u[n-1, i]
        else:
            u[n, i] = (S(i)**2) * (- 2*u[n-1, i] + u[n-1, i-1]) + 2*u[n-1, i]
        if n != 1:
            u[n, i] -= u[n-2, i]

u_plot_S1 = []

for i in range(200):
    u_plot_S1.append(u[int(195/0.775), i])

t1 = np.arange(0, 200, 1)

plt.figure()
plt.plot(t1, u_plot_S1, 'k')
plt.axvline(color='k', ls='--', x=140, ymin=-1, ymax=1)
plt.text(150, -0.4, "S = 0.25")
plt.text(115, -0.4, "S = 1")
plt.xlabel("Coordenada i da malha")
plt.ylabel("Funcao de onda u(i)")

plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math

# Definicao dos numeros de Courant e do vetor para plotagem
S = [1, 0.99, 0.5]
aux = []
u = {}
b = 20


# Execucao do algoritmo para todos os valores de S
def gaussian(n, S):
    return math.e**(-(((n-50/S)/(20/S))**2))


for s in S:
    x = []
    u_plot = []
    N = int(200/s)
    for i in range(math.ceil(100/s)):   # Sinal da fonte
        x.append(gaussian(i, s))

    for n in range(N):
        if n < 100/s:
            u[n, 0] = x[n]
        else:
            u[n, 0] = 0

    for i in range(1, 200):
        u[0, i] = 0

    for n in range(1, N):           # Execucao do algoritmo FDTD em si
        j = 1 if n < 100/s else 0
        for i in range(j, 200):
            if (i != 0 and i != 199):
                u[n, i] = (s**2) * (u[n-1, i+1] - 2*u[n-1, i] +
                                    u[n-1, i-1]) + 2*u[n-1, i]
            elif i == 0:
                u[n, i] = (s**2) * (u[n-1, i+1] - 2*u[n-1, i]) + 2*u[n-1, i]
            else:
                u[n, i] = (s**2) * (- 2*u[n-1, i] + u[n-1, i-1]) + 2*u[n-1, i]
            if n != 1:
                u[n, i] -= u[n-2, i]
    for i in range(200):
        u_plot.append(u[int(190/s), i])
    aux.append(u_plot)

# Plotagem do gráfico
t1 = np.arange(0, 200, 1)

fig, axs = plt.subplots(3)

axs[0].plot(t1, aux[0], 'k', label="S = 1")
axs[1].plot(t1, aux[1], 'k--', label="S = 0.99")
axs[2].plot(t1, aux[2], 'r--', label="S = 0.5")
axs[2].set_xlabel("Coordenada i da malha")
axs[1].set_ylabel("Funcao de onda u(i)")
for ax in axs:
    ax.legend(loc="upper left")

plt.show()

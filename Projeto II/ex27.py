import matplotlib.pyplot as plt
import numpy as np

# Definicao dos numeros de Courant e do vetor para plotagem
S = [1, 0.5]
aux = []

# Execucao do algoritmo para todos os valores de S
for s in S:
    u = {}
    u_plot = []
    N = int(200/s)
    for n in range(N):          # Sinal da fonte
        if n < 40/s:
            u[n, 0] = 1
        else:
            u[n, 0] = 0

    for i in range(1, 200):
        u[0, i] = 0

    for n in range(1, N):       # Execucao do algoritmo FDTD em si
        j = 1 if n < 40/s else 0
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
        u_plot.append(u[int(160/s), i])
    aux.append(u_plot)

# Plotagem do gráfico
t1 = np.arange(0, 200, 1)

plt.figure()
plt.plot(t1, aux[0], 'r--', label="S = 1")
plt.plot(t1, aux[1], 'k', label="S = 0.5")
plt.xlabel("Coordenada i da malha")
plt.ylabel("Funcao de onda u(i)")
plt.legend(loc="upper left")

plt.show()

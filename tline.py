import matplotlib.pyplot as plt
import numpy as np
import time

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(x)

c = 299792458  # velocidade da luz no vacuo (m/s)
l = 10000  # comprimento da linha de transmissao (m)
uf = 0.9 * c  # velocidade do sinal de tensao (m/s)
t_estac = 10 * l / uf
DeltaZ = l / 100
DeltaT = DeltaZ / uf
Kmax = 100
Nmax = int(t_estac / DeltaT)
Z0 = 50.0  # impedancia caracteristica
Zg = 75.0  # impedancia interna da fonte

c = 299792458  # velocidade da luz no vacuo (m/s)
l = 10000  # comprimento da linha de transmissao (m)
uf = 0.9 * c  # velocidade do sinal de tensao (m/s)
t_estac = 10 * l / uf
DeltaZ = l / 100
DeltaT = DeltaZ / uf * 0.5
Kmax = 100
Nmax = int(t_estac / DeltaT)
Z0 = 50.0  # impedancia caracteristica
Vg = 2  # tensao da fonte
Rs = 75.0  # impedancia interna da fonte
Rl = 100

C = 1 / (Z0 * uf)
L = Z0 * Z0 * C

V = {}  # tensao na linha de transmissao
V_ = {}  # tensao calculada para simplificação de contas
I = {}  # corrente na linha de transmissao

# constantes
c1 = 2 * DeltaT / (Rs * C * DeltaZ)
c2 = 2 * DeltaT / (Rl * C * DeltaZ)
c3 = DeltaT * DeltaT / (L * C * DeltaZ * DeltaZ)

# condicoes iniciais no tempo 0
for k in range(0, Kmax):
    V_[k, 0] = 0
    if (k != Kmax - 1):
        I[k, 0] = 0

for n in range(1, Nmax):
    for k in range(Kmax):
        if k == 0:
            V_[k, n] = (1 - c1) * V_[k, n - 1] - 2 * I[k, n - 1] + 2 / Rs * Vg
        elif k == Kmax - 1:
            V_[k, n] = (1 - c2) * V_[k, n - 1] + 2 * I[k - 1, n - 1]
        else:
            V_[k, n] = V_[k, n - 1] - (I[k, n - 1] - I[k - 1, n - 1])
    for k in range(Kmax - 1):
        I[k, n] = I[k, n - 1] - c3 * (V_[k + 1, n] - V_[k, n])

for n in range(Nmax):
    for k in range(Kmax - 1):
        print(I[k, n], " ", end='')
    print()

""" Modelo antigo comentado. (pode apagar se quiser)
print(V_{0})
x = np.linspace(0, l, l/DeltaZ)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, V[0], 'b-')

for Vt in V:
    line1.set_ydata(Vt)
    fig.canvas.draw()
    time.sleep(0.1)
"""

#Pega os dados do t=0, que serão plotados
VFixedTime = []
for k in range(Kmax):
    VFixedTime.append(V_[k, 0])

IFixedTime = []
for k in range(Kmax-1):
    IFixedTime.append(I[k, 0])

#Começa a plotagem
xV = np.linspace(0, l, l/DeltaZ)#Seta o eixo horizontal para cada valor discreto da distância
plt.ion()#Define o gráfico como interativo
fig,axs = plt.subplots(2)
lineV, = axs[0].plot(xV, VFixedTime, 'b-')
xI = x[:-1]
lineI, = axs[1].plot(xI, IFixedTime, 'b-')
axs[0].set_title("Tensão")
axs[1].set_title("Corrente")

for N in range(Nmax):
    VFixedTime = []#Reseta o vetor
    IFixedTime = []
    for k in range(Kmax):
        VFixedTime.append(V_[k, N])
    for k in range(Kmax-1):
        IFixedTime.append(I[k, N])
    lineV.set_ydata(VFixedTime)
    fig.canvas.draw()
    #time.sleep(0.001)


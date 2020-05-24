import matplotlib.pyplot as plt
import numpy as np
import time

c = 299792458           # velocidade da luz no vacuo (m/s)
l = 10000               # comprimento da linha de transmissao (m)
uf = 0.9 * c            # velocidade do sinal de tensao (m/s)
t_estac = 10 * l / uf
DeltaZ = l / 100
DeltaT = DeltaZ / uf * 0.5
Kmax = 100
Nmax = int(t_estac / DeltaT)
Z0 = 50.0               # impedancia caracteristica  
Vg = 2                  # tensao da fonte
Rs = 75.0               # impedancia interna da fonte   
Rl = 1/np.Inf

C = 1 / (Z0 * uf)
L = Z0 * Z0 * C

V = {}                  # tensao na linha de transmissao
V_ = {}                 # tensao calculada para simplificacao de contas
I = {}                  # corrente na linha de transmissao

# constantes
c1 = 2 * DeltaT / (Rs * C * DeltaZ)
if(Rl!=0):
    c2 = 2 * DeltaT / (Rl * C * DeltaZ)
else:
    c2 = 0
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
    for k in range(Kmax):
        V[k,n] = DeltaT * V_[k,n]/(C*DeltaZ)

#Pega os dados do t=0, que serao plotados
VFixedTime = []
for k in range(Kmax):
    VFixedTime.append(V[k, 0])

IFixedTime = []
for k in range(Kmax-1):
    IFixedTime.append(I[k, 0])

#Comeca a plotagem
xV = np.linspace(0, l, l/DeltaZ)    #Seta o eixo horizontal para cada valor discreto da distancia
plt.ion()                           #Define o grafico como interativo
fig,axs = plt.subplots(2)
lineV, = axs[0].plot(xV, VFixedTime, 'b-')
xI = np.linspace(0, l-DeltaZ, l/DeltaZ -1)
lineI, = axs[1].plot(xI, IFixedTime, 'b-')
axs[0].set_title("Tensao")
axs[1].set_title("Corrente")

axs[0].set(xlabel = 'Posicao z em metros', ylabel = 'Tensao em volts')

axs[0].set_ylim([-3,3])
#axs[1].set_xlim([0,50])
axs[1].set_ylim([-0.2,0.2])

for N in range(Nmax):
    VFixedTime = []                 #Reseta o vetor
    IFixedTime = []
    for k in range(Kmax):
        VFixedTime.append(V[k, N])
    for k in range(Kmax-1):
        IFixedTime.append(I[k, N])
    lineV.set_ydata(VFixedTime)
    lineI.set_ydata(IFixedTime)
    fig.canvas.draw()
    #time.sleep(0.001)


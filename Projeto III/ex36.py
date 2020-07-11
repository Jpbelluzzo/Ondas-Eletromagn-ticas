# import das bibliotecas
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0
import numpy as np

tam = 150
DeltaX = 1                      # infinitesimo de espaco
DeltaT = 1.01 * DeltaX / c             # infinitesimo de tempo
sigma = 0
sigma_ = 0
mu = mu_0
epsilon = epsilon_0
Kmax = int(tam/DeltaX)            # numero de amostras no espaco
Nmax = int(2*(tam/c)/DeltaT)      # numero de amostras no tempo

Ez = {}
Hy = {}

# constantes
Ca = (1-sigma*DeltaT/(2*epsilon))/(1+sigma*DeltaT/(2*epsilon))
Cb = (DeltaT/(epsilon*DeltaX))/(1+sigma*DeltaT/(2*epsilon))
Da = (1-sigma_*DeltaT/(2*mu))/(1+sigma_*DeltaT/(2*mu))
Db = (DeltaT/(mu*DeltaX))/(1+sigma_*DeltaT/(2*mu))

# Condicoes iniciais

# Ez = 0 no tempo inicial
for k in range(Kmax):
    Ez[k, 0] = 0

# Valores relacionados a fonte (i = 0)
for n in range(Nmax):
    if n < 40:
        Ez[0, n] = 1
    else:
        Ez[0, n] = 0

# No limite direito, Ez = 0 => condutor eletrico perfeito
for n in range(Nmax):
    Ez[Kmax, n] = 0

# Atribui 0 para Hy no tempo n = 0
for i in range(Kmax):
    Hy[i, 0] = 0

# Equacoes do FDTD
'''
Hy[i,n] = Da * Hy[i, n-1] + Db * (Ez[i, n] - Ez[i-1, n])
Ez[i,n] = Ca * Ez[i, n-1] + Cb * (Hy[i, n-1] - Hy[i-1, n-1])
'''

# Implementacao do FDTD
for n in range(1, Nmax):
    for i in range(1, Kmax):
        Ez[i, n] = Ca * Ez[i, n-1] - Cb * Hy[i-1, n-1] + Cb * Hy[i, n-1]
    for i in range(Kmax):
        Hy[i, n] = Da * Hy[i, n-1] + Db * (Ez[i+1, n] - Ez[i, n])

# Plotagem

# Vetores de plots
Ez_plot1 = []   # Antes da alcancar o limite direito
Ez_plot2 = []   # Depois de alcancar o limite direito

# Para a plotagem de Hy, deve-se alterar o range do loop e o tamanho
# do np.arange de Kmax para Kmax - 1, alem de alterar o vetor Ez para Hy
#
# Em N = 150, o pulso atinge o limite direito da malha
for k in range(Kmax):
    Ez_plot1.append(Ez[k, 120])  # N < 150
    Ez_plot2.append(Ez[k, 250])  # N > 150

# Definicao do eixo x
t1 = np.arange(0, Kmax, 1)

fig = plt.figure(1)

aux1 = fig.add_subplot(211)
aux1.title.set_text("n = 120")

plt.ylabel('Ez')
plt.xlabel("Coordenada i da malha")
plt.plot(t1, Ez_plot1, 'k')
plt.grid(True)

aux2 = fig.add_subplot(212)
aux2.title.set_text("n = 250")

plt.ylabel('Ez')
plt.xlabel("Coordenada i da malha")
plt.plot(t1, Ez_plot2, 'k')
plt.grid(True)
plt.show()

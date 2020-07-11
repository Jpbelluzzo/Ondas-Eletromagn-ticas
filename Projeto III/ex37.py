# import das bibliotecas
import numpy as np
from scipy.constants import speed_of_light, mu_0, epsilon_0
import matplotlib.pyplot as plt
import matplotlib.animation as animation    # biblioteca do plot 3D-animado
from mpl_toolkits.mplot3d import Axes3D     # biblioteca do plot 3D-animado
import seaborn as sns               # biblioteca do plot em heatmap

# OBS 1. Algumas bibliotecas podem nao ser utilizadas
# dependendo do plot desejado. Porem, por simplicidade,
# todas sao importadas inicialmente.

# OBS 2. Alem disso, o linter da PEP 8, por algum motivo,
# pode indicar a nao utilizacao da "Axes3D", mesmo quando
# a plotagem animada eh escolhida. Eh valido ressaltar que
# o programa gera um erro caso esse import nao seja feito,
# ja que essa biblioteca esta relacionada com um parametro
# da plotagem 3D.

# Inicio do algoritmo


# definicao da fonte
# pulso retangular de amplitude 1
# e 20*DeltaT de duracao
def fonte(n):
    if n < 20:
        return 1
    else:
        return 0


tam = 100                       # tamanho do espaco
DeltaX = 1                      # infinitesimo de espaco
DeltaT = DeltaX / (np.sqrt(2)*speed_of_light)  # infinitesimo de tempo
sigma = 0
sigma_ = 0
mu = mu_0
epsilon = epsilon_0
Kmax = int(tam/DeltaX)      # numero de amostras no espaco
Nmax = 100      # numero de amostras no tempo


# constantes
Ca = (1-sigma*DeltaT/(2*epsilon))/(1+sigma*DeltaT/(2*epsilon))
Cb = (DeltaT/(epsilon*DeltaX))/(1+sigma*DeltaT/(2*epsilon))
Da = (1-sigma_*DeltaT/(2*mu))/(1+sigma_*DeltaT/(2*mu))
Db = (DeltaT/(mu*DeltaX))/(1+sigma_*DeltaT/(2*mu))

# cria matrizes
Ez = np.empty((Nmax, Kmax+1, Kmax+1))
Hx = np.empty((Nmax, Kmax+1, Kmax))
Hy = np.empty((Nmax, Kmax, Kmax+1))

# condicoes iniciais
Ez[0] = np.zeros((Kmax+1, Kmax+1))
Hx[0] = np.zeros((Kmax+1, Kmax))
Hy[0] = np.zeros((Kmax, Kmax+1))

# condicoes de contorno
for n in range(Nmax):
    for i in range(Kmax+1):
        Ez[n, i, 0] = 0
for n in range(Nmax):
    for j in range(Kmax+1):
        Ez[n, 0, j] = 0
for n in range(Nmax):
    for i in range(Kmax+1):
        Ez[n, i, Kmax] = 0
for n in range(Nmax):
    for j in range(Kmax+1):
        Ez[n, Kmax, j] = 0

# equacoes com os indices adaptados
#
# Ez[n,i,j] = Ca * Ez[n-1,i,j] + Cb * (Hy[n-1,i,j] - Hy[n-1,i-1,j]
#                                    + Hx[n-1,i,j-1] - Hx[n-1,i,j])
# Hx[n,i,j] = Da * Hx[n-1,i,j] + Db *(Ez[n,i,j] - Ez[n,i,j+1])
# Hy[n,i,j] = Da * Hy[n-1,i,j] + Db * (Ez[n,i+1,j] - Ez[n,i,j])

# implementacao do FDTD em si
for n in range(1, Nmax):
    for i in range(1, Kmax):
        for j in range(1, Kmax):
            Ez[n, i, j] = Ca * Ez[n-1, i, j] \
                          + Cb * (Hy[n-1, i, j] - Hy[n-1, i-1, j]) \
                          + Cb*(Hx[n-1, i, j-1] - Hx[n-1, i, j])
    Ez[n, int(Kmax/2), int(Kmax/2)] = fonte(n)
    for i in range(Kmax+1):
        for j in range(Kmax):
            Hx[n, i, j] = Da * Hx[n-1, i, j] + Db * (Ez[n, i, j]
                                                     - Ez[n, i, j+1])
    for i in range(Kmax):
        for j in range(Kmax+1):
            Hy[n, i, j] = Da * Hy[n-1, i, j] \
                          + Db * (Ez[n, i+1, j] - Ez[n, i, j])

# Representacao dos resultados

# Remova os comentarios do tipo de plot
# desejado: heatmap ou 3D-animado

# Plot em mapas de calor

# Insira em Ez[n], Hx[n] e Hy[n] um tempo n, tal que 0 < n < 100,
# sendo que a borda eh atingida proximo de n = 70.
# Para observar a reflexao, eh sugerido n = -1 (ultimo n possivel).
"""
# Plot do campo Ez
plt.figure(1)
sns.heatmap(Ez[65], xticklabels=10, yticklabels=10)
plt.title("Campo Ez")
plt.ylabel("Coordenada i da malha")
plt.xlabel("Coordenada j da malha")

# Plot de Hx
plt.figure(2)
sns.heatmap(Hx[65], xticklabels=10, yticklabels=10)
plt.title("Campo Hx")
plt.ylabel("Coordenada i da malha")
plt.xlabel("Coordenada j da malha")

# Plot de Hy
plt.figure(3)
sns.heatmap(Hy[65], xticklabels=10, yticklabels=10)
plt.title("Campo Hy")
plt.ylabel("Coordenada i da malha")
plt.xlabel("Coordenada j da malha")

plt.show()

"""

# Plotagem animada

# Para nao aumentar muito o tempo de execucao, a cada
# execucao do programa, eh plotada a animacao de um dos
# campos.


def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:, :, frame_number], cmap="magma")


fps = 10        # frame per sec
frn = Nmax      # frame number of the animation
x = np.arange(0, Kmax)
y = np.arange(0, Kmax)
x, y = np.meshgrid(x, y)
time = np.arange(0, Nmax)
zarray = np.zeros((Kmax, Kmax, frn))

# Defina aqui o campo a ser representado na animacao
for i in range(frn):
    for j in x:
        for k in y:
            zarray[j, k, i] = Ez[i, j, k]   # campo a ser plotado

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot = [ax.plot_surface(x, y, zarray[:, :, 0], color='0.75', rstride=1,
                        cstride=1)]

ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot),
                              interval=500/fps)

plt.show()

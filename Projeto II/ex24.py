# Inclusao de bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import math

# Definicao do numero de Courant e do N de transicao
S = 1/math.sqrt(2)
Ntran = (2*math.pi*S/math.acos(1-2*S**2))


# Definicao de zeta
def zeta(N, S):
    return 1+(1/S)**2 * (math.cos(2*math.pi*S/N)-1)


# Definicao da velocidade de fase numerica normalizada
def vfase_normal(N, S):
    if(N >= Ntran):
        return 2*math.pi/(N*math.acos(zeta(N, S)))
    else:
        return 2/N


# Definicao da atenuacao
def atenuacao(N, S):
    if(N >= Ntran):
        return 0
    else:
        return -math.log(-zeta(N, S)-math.sqrt(zeta(N, S)**2 - 1))


v = []
aten = []
N = 1

# Calculo dos parametros
while N <= 10:
    v.append(vfase_normal(N, S))
    aten.append(atenuacao(N, S))
    N += 0.2

# Configuracao dos graficos e plotagem
t1 = np.arange(1.0, 10.2, 0.2)

fig, ax1 = plt.subplots()

ax1.set_xlabel(
    'Densidade de amostragem da malha'
    '(pts por comprimento de onda no espaço livre)'
)
ax1.set_ylabel('Constante de Atenuação(nepers/célula da malha)',
               color='r')
ax1.set_ylim(0, 3)
ax1.plot(t1, aten, 'r--')
ax1.tick_params(axis='y', labelcolor='r')

ax2 = ax1.twinx()
ax2.set_ylabel('Velocidade de fase numérica (normalizada por c)',
               color='k')
ax2.plot(t1, v, color='k')
ax2.tick_params(axis='y', labelcolor='k')
ax2.set_xlim(1, 10)

fig.tight_layout()
plt.show()

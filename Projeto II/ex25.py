import matplotlib.pyplot as plt
import numpy as np
import math

S = 1/2
c = 299792458
Ntran = (2*math.pi*S/math.acos(1-2*S**2))


def zeta(N, S):
    return 1+(1/S)**2 * (math.cos(2*math.pi*S/N)-1)


def vfase(N, S):
    if(N >= Ntran):
        return 2*math.pi*c/(N*math.acos(zeta(N, S)))
    else:
        return 2*c/N


v = []
v_erro = []
N = 3

while N <= 82:
    v.append(vfase(N, S))
    v_erro.append(abs(vfase(N, S)-c)*100/c)
    N += 1

t1 = np.arange(2, 82, 1)

plt.plot(t1, v_erro, 'k')
plt.ylabel('Erro da velocidade de fase (%)')
plt.xlabel(
    'Densidade de amostragem da malha'
    '(pts por comprimento de onda no espaço livre)'
)
plt.yscale("log")
plt.grid(True)

plt.show()

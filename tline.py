c = 299792458  #velocidade da luz no vacuo (m/s)
l = 10000       #comprimento da linha de transmissao (m)
uf = 0.9*c      #velocidade do sinal de tensao (m/s)
t_estac = 10*l/uf
DeltaZ = l/100
DeltaT = DeltaZ/uf
Kmax = 100
Nmax = int(t_estac/DeltaT)
Z0 = 50.0     # impedancia caracteristica
Zg = 75.0     # impedancia interna da fonte

C = 1/(Z0*uf)
L = Z0*Z0*C

c1 = -DeltaT/(DeltaZ*L)
c2 = 1.0
c3 = -DeltaT/(DeltaZ*C)
c4 = 1.0

V = {}     # tensao na linha de transmissao
I = {}      # corrente na linha de transmissao
#Vinst = []  # tensao instantanea
#Iinst = []  # corrente instantanea
Vg = 1       # tensao da fonte

# V(0,0) atribuido
V[0,0] = (Z0*Vg/(Zg+Z0))
# V(k,0) atribuidos
for k in range(1,Kmax):
    V[k,0] = 0.0

# I(0,0) atribuido
I[0,0] = (Vg/(Zg+Z0))
# I(k,0) atribuidos
for k in range(1,Kmax):
    I[k,0] = 0.0

'''for n in range(1,Nmax):
    for k in range(0,Kmax):
        if k == 0:
            I[k,n] = c1*(V[k,n-1]) + c2*I[k,n-1]
        elif k != (Kmax-1):
            I[k,n] = c1*(V[k,n-1]-V[k-1,n-1]) + c2*I[k,n-1]
        else:
            I[k,n] = c1*(-V[k-1,n-1]) + c2*I[k,n-1]
    for k in range(0,Kmax):
        if k != Kmax-1:
            V[k,n] = c3 * (I[k+1,n] - I[k,n]) + c4 * V[k,n-1]
        else:
            V[k,n] = c4 * V[k,n-1]'''

for n in range(1,Nmax):
    for k in range(0,Kmax):
        if k == 0:
            I[k,n] = c1 * (V[k,n-1]) + c2 * I[k,n-1]
        else:
            I[k,n] = c1 * (V[k,n-1] - V[k-1,n-1]) + c2 * I[k,n-1]
    for k in range(0,Kmax):
        if k == Kmax-1:
            V[k,n] = c4 * V[k,n-1]
        else:
            V[k,n] = c3 * (I[k+1,n] - I[k,n]) + c4 * V[k,n-1]

for n in range(50):
    for k in range(Kmax):
        print(V[k,n], " ", end='')
    print()
    
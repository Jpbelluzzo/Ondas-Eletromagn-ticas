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

V = []      # tensao na linha de transmissao
I = []      # corrente na linha de transmissao
Vinst = []  # tensao instantanea
Iinst = []  # corrente instantanea
Vg = 1       # tensao da fonte

# V(0,0) atribuido
Vinst.append(Z0*Vg/(Zg+Z0))
# V(k,0) atribuidos
for k in range(1,Kmax):
    Vinst.append(0)
V.append(Vinst)

# I(0,0) atribuido
Iinst.append(Vg/(Zg+Z0))
# I(k,0) atribuidos
for k in range(1,Kmax):
    Iinst.append(0)
I.append(Iinst)


for n in range(1,Nmax):
    Vinst = []
    Iinst = []

    for k in range(0,Kmax):
        if k != (Kmax-1):
            iN1 = c1*(V[n-1][k+1]-V[n-1][k]) + c2*I[n-1][k]
        else:
            iN1 = c1*(-V[n-1][k]) + c2*I[n-1][k]
        Iinst.append(iN1)
    I.append(Iinst)
    for k in range(0,Kmax):
        if k != Kmax-1:
            vN1 = c3 * (I[n][k+1] - I[n][k]) + c4 * V[n-1][k]
        else:
            vN1 = c4 * V[n-1][k]
        Vinst.append(vN1)
    V.append(Vinst)
    
print(V)


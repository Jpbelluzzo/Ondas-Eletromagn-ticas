DeltaZ = 
DeltaT =
Kmax = 
Nmax
Z0 = 50     # impedancia caracteristica
Zg = 75     # impedancia interna da fonte

V = []      # tensao na linha de transmissao
I = []      # corrente na linha de transmissao
Vinst = []  # tensao instantanea
Iinst = []  # corrente instantanea
Vg =        # tensao da fonte

# V(0,0) atribuido
for i in range(Kmax):
    Vinst.append(Z0*Vg/(Zg+Z0))
V.append(Vinst)

# I(0,0) atribuido
for i in range(Kmax):
    Iinst.append(Vg/(Zg+Z0))
I.append(Iinst)

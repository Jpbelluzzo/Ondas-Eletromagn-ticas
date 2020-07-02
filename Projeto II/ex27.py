import matplotlib.pyplot as plt
import numpy as np
import math

S = 1
u = {}

for i in range(200):
    if i<40:
        u[0,i] = 1
    else:
        u[0,i] = 0

for n in range(199):
    for i in range(200):
        if (i!=0 and i!=199):
            u[n+1,i] = (S**2) * (u[n,i+1]-2*u[n,i]+u[n,i-1]) + 2*u[n,i] 
        elif i==0:
            u[n+1,i] = (S**2) * (u[n,i+1]-2*u[n,i]) + 2*u[n,i] 
        else:
            u[n+1,i] = (S**2) * (-2*u[n,i]+u[n,i-1]) + 2*u[n,i]
        if n!=0: u[n+1,i]-=u[n-1,i]

u_plot = []

for i in range(200):
    u_plot.append(u[1,i])

t1 = np.arange(0, 200, 1)

plt.figure()
plt.plot(t1, u_plot, 'k')

plt.show()

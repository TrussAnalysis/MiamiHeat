import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

length = 50 # cm
alpha = 1 # cm2/s
pontos = 10
pos = [0, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0]
pre = [0, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0]
total = 30
delta_x = length/pontos
fourier = (alpha * 1)/ math.pow(delta_x,2)
x = range(0,55,5)
print(x)
for i in range(300):
    for j in range(1, len(pre)-1):
        plt.plot(x, pos)
        pos[j] = pre[j] + fourier*(pre[j+1] - 2*pre[j] + pre[j-1])
    for k in range (len(pos)):
        pre[k] = pos[k]
plt.show()
        
print(pos)

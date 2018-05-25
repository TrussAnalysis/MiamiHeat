import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
from Matrix import Matrix

# length = 50 # cm
# alpha = 1 # cm2/s
# pontos = 10
# pos = [0, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0]
# pre = [0, 20, 20, 20, 20, 20, 20, 20, 20, 20, 0]
# total = 30
# delta_x = length/pontos
# fourier = (alpha * 1)/ math.pow(delta_x,2)
# x = range(0,55,5)
# print(x)
# for i in range(300):
#     for j in range(1, len(pre)-1):
#         plt.plot(x, pos)
#         pos[j] = pre[j] + fourier*(pre[j+1] - 2*pre[j] + pre[j-1])
#     for k in range (len(pos)):
#         pre[k] = pos[k]
# plt.show()

# print(pos)

def solve(pre, alpha, length, pontos, iterations):
    deltaX = length/pontos
    fourier = (alpha * 1)/ math.pow(deltaX,2)
    pos = Matrix(pontos, pontos)
    
    #copy
    for i in range (pre.rows):
        for j in range (pre.cols):
            pos.data[i][j] = pre.data[i][j]

    #sponge bob
    for jkl in range(iterations):
        # shit that matters
        for i in range (1, pre.rows-1):
            for j in range (1, pre.cols-1):
                pos.data[i][j] = fourier*(pre.data[i+1][j] + pre.data[i-1][j] +
                                        pre.data[i][j+1] + pre.data[i][j-1]) +\
                                        ((1-4*fourier) * pre.data[i][j])
        
        # another useless copy
        for i in range (pre.rows):
            for j in range (pre.cols):
                pre.data[i][j] = pos.data[i][j]
    
    return pos


    
    
    

def analitical_solution(self, x, t, alpha, size):
    number_of_nodes = int(round(size / x))
    temperatures = []
    for i in range(number_of_nodes):
        temp = 80/math.pi
        k1 = ((math.pi**2)*alpha*t)/2500
        k2 = (math.pi*x)/50

        iteration = 0
        n = 1
        while n <= 100:
            iteration += (1/n) * (math.e**(k1*(-n**2))) * (math.sin(n*k2))
            n +=2
        
        temp *= iteration
        temperatures.append(temp)

    print(temperatures)
    return temperatures
    

pontos = 5
alpha = 9.4967 * 10**(-5)
length = 0.4
chapa = Matrix(pontos, pontos)

for i in range (chapa.rows):
        for j in range (chapa.cols):
            if (i==0):
                chapa.data[i][j] = 100
                continue
            if(i == chapa.rows - 1):
                chapa.data[i][j] = 0
                continue
            if(j == 0):
                chapa.data[i][j] = 75
                continue
            if(j == chapa.cols - 1):
                chapa.data[i][j] = 50
                continue
            chapa.data[i][j] = 0
            

pos = solve(chapa, alpha, length, pontos, 1000)
pos.console()


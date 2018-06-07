import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
from Matrix import Matrix
import math
# plt.switch_backend('Qt5Agg')
def matriciones(it, pontos):
    lista = []
    for i in range (it):
        m = Matrix(pontos, pontos)
        lista.append(m)
    return lista

def makeBoard(height, width, top, bot, left, right, overall):
    chapa = Matrix(height, width)

    for i in range (chapa.rows):
        for j in range (chapa.cols):
            if (i==0):
                chapa.data[i][j] = top
                continue
            if(i == chapa.rows - 1):
                chapa.data[i][j] = bot
                continue
            if(j == 0):
                chapa.data[i][j] = left
                continue
            if(j == chapa.cols - 1):
                chapa.data[i][j] = right
                continue
            chapa.data[i][j] = overall
    return chapa

        


def solve(pre, alpha, length, pontos, iterations):
    list_of_matrix = matriciones(iterations, pontos)
    deltaX = length/pontos
    fourier = (alpha * 1)/ math.pow(deltaX, 2)
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
                list_of_matrix[jkl].data[i][j] = pos.data[i][j]

    
    return pos, list_of_matrix



pontos = 20
alpha = 9.4967 * 10**(-5)
# alpha = 9.4967 * 10**(-6)
length = 0.4

chapa = makeBoard(20,20,100,0,75,50,0)


it = 200
pos, list_of_matrix = solve(chapa, alpha, length, pontos, it)

# list_of_matrix[it-1].console()

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.1, bottom=0.1)
min0 = 0
max0 = 25000

inter = None
if(pontos >= 10):
    inter = 'gaussian'

im1 = ax.imshow(list_of_matrix[0].data, cmap='jet', interpolation=inter)
fig.colorbar(im1)

axcolor = 'lightgoldenrodyellow'
axmax  = fig.add_axes([0.25, 0.01, 0.65, 0.03], axisbg=axcolor)

smax = Slider(axmax, 'Segundos', 0, it-1, valinit=0)

def update(val):
    im1.set_data(list_of_matrix[int(smax.val)].data)
    fig.canvas.draw()
smax.on_changed(update)

plt.show()
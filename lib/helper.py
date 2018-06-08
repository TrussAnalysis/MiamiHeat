import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
from Matrix import Matrix
import math
# plt.switch_backend('Qt5Agg')

def fillMatrix(it, pontos):
    lista = []
    for i in range (it):
        m = Matrix(pontos, pontos)
        lista.append(m)
    return lista
    
#Prepare board to be used
def buildBoard(points, top, bot, left, right, overall):
    board = Matrix(points, points)

    # Check if any border is isolated
    limit_top = top
    limit_bot = bot
    limit_right = right
    limit_left = left
    if top == "isolado":
        limit_top = 0
    if bot == "isolado":
        limit_bot = 0
    if right == "isolado":
        limit_right = 0
    if left == "isolado":
        limit_left = 0
    
    # Build board matrix
    for i in range (board.rows):
        for j in range (board.cols):
            if (i==0):
                board.data[i][j] = limit_top
                continue
            if(i == board.rows - 1):
                board.data[i][j] = limit_bot
                continue
            if(j == 0):
                board.data[i][j] = limit_left
                continue
            if(j == board.cols - 1):
                board.data[i][j] = limit_right
                continue
            board.data[i][j] = overall
    return board

# Use numeric methods to solve system dynamics 
def solve(pre, alpha, length, pontos, iterations, top, bot, right, left):
    list_of_matrix = fillMatrix(iterations, pontos)
    deltaX = length/pontos
    fourier = (alpha * 1)/ math.pow(deltaX, 2)
    pos = Matrix(pontos, pontos)
    tol = 0.001

    
    # Copy
    for i in range (pre.rows):
        for j in range (pre.cols):
            pos.data[i][j] = pre.data[i][j]

    # Calculate borders if they are isolated
    for jkl in range(iterations):
        aceitos = 0
        
        if(isinstance(top, str)):
            for j in range(1,pre.cols - 1):
                # if j==1:
                #     pos.data[0][j] = fourier * ((pre.data[1][j] * 2) + pre.data[0][j+1] + (1- 4*fourier) * pre.data[0][j])
                # elif j == pre.cols-2:
                #     pos.data[0][j] = fourier * ((pre.data[1][j] * 2) + pre.data[0][j-1]) + (1- 4*fourier) * pre.data[0][j]
                # else:
                pos.data[0][j] = fourier * ((pre.data[1][j] * 2) + pre.data[0][j+1] + pre.data[0][j-1]) + (1- 4*fourier) * pre.data[0][j]
        
        if(isinstance(bot, str)):
            for j in range(1,pre.cols - 1):
                # if j==1:
                #     pos.data[pre.cols-1][j] = fourier * ((pre.data[pre.cols-2][j] * 2) + pre.data[pre.cols-1][j+1] + (1- 4*fourier) * pre.data[pre.cols-1][j])
                # elif j==pre.cols-2:
                #     pos.data[pre.cols-1][j] = fourier * ((pre.data[pre.cols-2][j] * 2) + pre.data[pre.cols-1][j-1]) + (1- 4*fourier) * pre.data[pre.cols-1][j]
                # else:
                pos.data[pre.cols-1][j] = fourier * ((pre.data[pre.cols-2][j] * 2) + pre.data[pre.cols-1][j+1] + pre.data[pre.cols-1][j-1]) + (1- 4*fourier) * pre.data[pre.cols-1][j]
        
        if(isinstance(right, str)):
            for i in range(1,pre.cols - 1):
                # if i==1:
                #     pos.data[i][pre.cols-1] = fourier * ((pre.data[i][pre.cols-2] * 2) + pre.data[i+1][pre.cols-1]\
                #                  + (1- 4*fourier) * pre.data[i][pre.cols-1])
                # elif (i==pre.cols-2):
                #     pos.data[i][pre.cols-1] = fourier * ((pre.data[i][pre.cols-2] * 2) + pre.data[i-1][pre.cols-1])\
                #                  + (1- 4*fourier) * pre.data[i][pre.cols-1]
                # else:
                pos.data[i][pre.cols-1] = fourier * ((pre.data[i][pre.cols-2] * 2) + pre.data[i+1][pre.cols-1] + pre.data[i-1][pre.cols-1])\
                            + (1- 4*fourier) * pre.data[i][pre.cols-1]

        if(isinstance(left, str)):
            for i in range(1,pre.cols - 1):
                # if i==1:
                #     pos.data[i][0] = fourier * ((pre.data[i][1] * 2) + pre.data[i+1][0]\
                #                  + (1- 4*fourier) * pre.data[i][0])
                # elif i==pre.cols-2:
                #     pos.data[i][0] = fourier * ((pre.data[i][1] * 2) + pre.data[i-1][0])\
                #                  + (1- 4*fourier) * pre.data[i][0]
                # else:
                pos.data[i][0] = fourier * ((pre.data[i][1] * 2) + pre.data[i+1][0] + pre.data[i-1][0])\
                                + (1- 4*fourier) * pre.data[i][0]
        
        
                                 
        # Calculate temperature of whole board
        for i in range (1, pre.rows-1):
            for j in range (1, pre.cols-1):
                pos.data[i][j] = fourier * (pre.data[i+1][j] + pre.data[i-1][j] +
                                        pre.data[i][j+1] + pre.data[i][j-1]) +\
                                        ((1-4*fourier) * pre.data[i][j])
                if pos.data[i][j] > 0:
                    erro = (pos.data[i][j] - pre.data[i][j])/pos.data[i][j]
                    if(erro <= tol):
                        aceitos += 1
        
        # Send to clean matrix
        for i in range (pre.rows):
            for j in range (pre.cols):
                pre.data[i][j] = pos.data[i][j]
                list_of_matrix[jkl].data[i][j] = pos.data[i][j]

        # print("Pontos de dentro: ", ((pre.rows-2)*(pre.rows-2)))
        # print("Aceitos: ", aceitos)

        if aceitos == ((pre.rows-2)*(pre.rows-2)):
            break
    
    return pos, list_of_matrix, jkl

# Plot board into MatPlotLib with time sliders
def plotBoard(list_of_matrix, pontos, it):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.25, bottom=0.25)
    min0 = 0
    max0 = 25000

    inter = None
    if(pontos >= 10):
        inter = 'gaussian'

    im1 = ax.imshow(list_of_matrix[0].data, cmap='jet', interpolation=inter)

    fig.colorbar(im1)

    axcolor = 'lightgoldenrodyellow'
    axmax  = fig.add_axes([0.25, 0.15, 0.65, 0.03])#, axisbg=axcolor)

    t = Slider(axmax, 'Tempo', 0, it-1, valinit=0, valfmt='%d')

    def update(val):
        im1.set_data(list_of_matrix[int(t.val)].data)
        fig.canvas.draw()
    t.on_changed(update)

    plt.show()

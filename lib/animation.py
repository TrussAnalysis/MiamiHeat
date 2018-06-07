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

def openFile(path):
    f = open(path, 'r')
    linha = f.readline()

    while("Tempo" not in linha):
        linha = f.readline()
    l = linha.split( )
    time = l[1]
    print("Tempo: ",time)

    while("Tamanho" not in linha):
        linha = f.readline()
    l = linha.split( )
    length = l[1]
    print("Tamanho: ",length)

    while("Pontos" not in linha):
        linha = f.readline()
    l = linha.split( )
    pontos = l[1]
    print("Pontos: ",pontos)

    while("cima" not in linha):
        linha = f.readline()
    l = linha.split( )
    top = l[3]
    print("Cima: ",top)

    while("baixo" not in linha):
        linha = f.readline()
    l = linha.split( )
    bot = l[3]
    print("Baixo: ",bot)

    while("esquerda" not in linha):
        linha = f.readline()
    l = linha.split( )
    left = l[3]
    print("Esquerda: ",left)

    while("direita" not in linha):
        linha = f.readline()
    l = linha.split( )
    right = l[3]
    print("Direita: ",right)

    while("centro" not in linha):
        linha = f.readline()
    l = linha.split( )
    center = l[3]
    print("Centro: ", center)
    
    top=int(top) if top.isdigit() else "isolado"
    bot=int(bot) if bot.isdigit() else "isolado"
    left=int(left) if left.isdigit() else "isolado"
    right=int(right) if right.isdigit() else "isolado"

    return int(time), float(length), int(pontos), top, bot, left, right, int(center)
    

def makeBoard(points, top, bot, left, right, overall):
    chapa = Matrix(points, points)

    top2 = top
    if top == "isolado":
        top2 = 0
    bot2 = bot
    if bot == "isolado":
        bot2 = 0
    right2 = right
    if right == "isolado":
        right2 = 0
    left2 = left
    if left == "isolado":
        left2 = 0
    
    
    for i in range (chapa.rows):
        for j in range (chapa.cols):
            if (i==0):
                chapa.data[i][j] = top2
                continue
            if(i == chapa.rows - 1):
                chapa.data[i][j] = bot2
                continue
            if(j == 0):
                chapa.data[i][j] = left2
                continue
            if(j == chapa.cols - 1):
                chapa.data[i][j] = right2
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
        
        
                                 
        # shit that matters
        for i in range (1, pre.rows-1):
            for j in range (1, pre.cols-1):
                pos.data[i][j] = fourier * (pre.data[i+1][j] + pre.data[i-1][j] +
                                        pre.data[i][j+1] + pre.data[i][j-1]) +\
                                        ((1-4*fourier) * pre.data[i][j])
        
        # another useless copy
        for i in range (pre.rows):
            for j in range (pre.cols):
                pre.data[i][j] = pos.data[i][j]
                list_of_matrix[jkl].data[i][j] = pos.data[i][j]

    
    return pos, list_of_matrix

it, lenght, pontos, top, bot, left, right, center = openFile("info.txt")

chapa = makeBoard(pontos, top, bot, left, right, center)

# pontos = 7
alpha = 9.4967 * 10**(-5)
# alpha = 9.4967 * 10**(-6)
# length = 0.4

# chapa = makeBoard(pontos,100,0,75,50,0)


# it = 200
it+=1
pos, list_of_matrix = solve(chapa, alpha, lenght, pontos, it)

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
axmax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

t = Slider(axmax, 'Tempo', 0, it-1, valinit=0, valfmt='%d')

def update(val):
    im1.set_data(list_of_matrix[int(t.val)].data)
    fig.canvas.draw()
t.on_changed(update)

plt.show()


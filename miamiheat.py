import getopt
import math
import sys

sys.path.insert(0, './lib')

from helper import *
from Matrix import Matrix

# import matplotlib
# # matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.widgets import Slider, Button, RadioButtons

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

def main(argv):
    inputfile = ''
    
    try:
        opts, args = getopt.getopt(argv, "h:i:", ["ifile="])
    except getopt.GetoptError:
        print('Usage is: main.py -i <inputfile> or -h for help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage is: main.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        else:
            print('An error ocurred, type "test.py -h for help"')
            sys.exit()
    
    if inputfile == '':
        print('Input file not found.')
        sys.exit()
    else:
        print('Input file is:', inputfile)

    it, lenght, pontos, top, bot, left, right, center = openFile(inputfile)
    board = buildBoard(pontos, top, bot, left, right, center)

    it = 200
    it+=1
    alpha = 9.4967 * 10**(-5)
    pos, list_of_matrix = solve(board, alpha, lenght, pontos, it, top, bot, left, right)

    plotBoard(list_of_matrix, pontos, it)

if __name__ == "__main__":
    main(sys.argv[1:])

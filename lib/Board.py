import sys
from Matrix import Matrix

class Board:
    # Dados da Placa
    # nao sei se ta certo ainda
    def __init__(self, height, width, top, bot, left, right, overall):
        self.H = height         #m
        self.L =  width         #m
        self.temp_top = top     #ºC
        self.temp_bot = bot     #ºC
        self.temp_left = left   #ºC
        self.temp_right = right #ºC

        chapa = Matrix(height, width)

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
                chapa.data[i][j] = overall
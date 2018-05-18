import sys
# from Matrix import *

class Board:
    # Dados da Placa
    # nao sei se ta certo ainda
    def __init__(self, height, width, top, bot, left, right):
        H = height #m
        L =  width #m
        # Material: Alumínio
        temp_top = top #ºC
        temp_bot = bot #ºC
        temp_left = left #ºC
        temp_right = right #ºC
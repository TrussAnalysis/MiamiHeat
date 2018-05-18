import sys
# from Matrix import *

class Fin:
    # Dados da Aleta
    def __init__(self):
        h = 100 #W/m²*K
        t_amb = 25 #ºC
        # Material: Alumínio
        p = 900 #kg/m
        k = 240 #W/m*K
        c = 896 #J/kg*K
        nodes_number = 15
        L = 0.1865 #m
        r = 0.012 #m
        # Tempo de simulação: 2 min
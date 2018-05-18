import sys, getopt
import math
sys.path.insert(0, './lib')
from Fin import Fin
from Board import Board
# from Matrix import *
# from File import FileIn, FileOut

def main(argv):
    # inputfile = ''
    # outputfile = ''
    # method = 'Gauss-Seidel'
    # iterations = 500
    # try:
    #     opts, args = getopt.getopt(argv, "hi:o:m:n:", ["ifile=", "ofile=", "method=", "iterations="])
    # except getopt.GetoptError:
    #     print('Usage is: main.py -i <inputfile> -o <outputfile> -m <method> -n <number of iterations> or test.py -h for help')
    #     sys.exit(2)
    # for opt, arg in opts:
    #     if opt == '-h':
    #         print('main.py -i <inputfile> -o <outputfile> -m <method> -n <number of iterations>')
    #         sys.exit()
    #     elif opt in ("-i", "--ifile"):
    #         inputfile = arg
    #     elif opt in ("-o", "--ofile"):
    #         outputfile = arg
    #     elif opt in ("-m", "--method"):
    #         method = arg
    #     elif opt in ("-n", "--iterations"):
    #         iterations = arg
    #     else:
    #         print('An error ocurred, type "test.py -h for help"')
    #         sys.exit()

    # print('Input file is:', inputfile)
    # print('Output file is:', outputfile)
    # print("Using {0} method". format(method))

    # output = FileOut(outputfile, truss, Matrix.toArray(displacement_matrix), reaction_forces, vector_names, stresses, strains)
    # output.writeOutputFile()

if __name__ == "__main__":
    main(sys.argv[1:])

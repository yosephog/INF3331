import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit
import argparse
from my_modul import *

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('xmin',type=float)
    parser.add_argument('xmax',type=float)
    parser.add_argument('ymin',type=float)
    parser.add_argument('ymax' ,type=float)
    parser.add_argument('width',type=int)
    parser.add_argument('height',type=int)
    parser.add_argument('maxiteration',type=int)
    parser.add_argument('choice',help="choice between python,numpy or numba")
    parser.add_argument('file_name',help='Name of the file for the image to be saved')
    args=parser.parse_args()
    if args.choice == 'python':
        liste=mandel_python(args.xmin,args.xmax,args.ymin,args.ymax,
        args.width,args.height,args.maxiteration)

        plt.imshow(liste, cmap = plt.cm.gist_stern,extent = (args.xmin,args.xmax,args.ymin,args.ymax))
        plt.savefig(args.file_name)
        plt.show()

    if args.choice == 'numpy':
        liste=mandel_numpy(args.xmin,args.xmax,args.ymin,args.ymax,
        args.width,args.height,args.maxiteration)

        plt.imshow(liste, cmap = plt.cm.gist_stern,extent = (args.xmin,args.xmax,args.ymin,args.ymax))
        plt.savefig(args.file_name)
        plt.show()

    if args.choice == 'numba':
        liste=mandel_numba(args.xmin,args.xmax,args.ymin,args.ymax,
        args.width,args.height,args.maxiteration)

        plt.imshow(liste, cmap = plt.cm.gist_stern,extent = (args.xmin,args.xmax,args.ymin,args.ymax))
        plt.savefig(args.file_name)
        plt.show()

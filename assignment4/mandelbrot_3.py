import numpy as np
import matplotlib.pyplot as plt
import time
from numba import jit

@jit(nopython=True)
def compute(c,maxiter):
    z=0
    for i in range(maxiter):
        z=z**2 + c

        if abs(z) > 2:
            return i
    return 0

@jit(nopython=True)
def mandel(xmin,xmax,ymin,ymax,width,height,maxiter):
    x=np.linspace(xmin,xmax,width)
    y=np.linspace(ymin,ymax,height)
    list=np.zeros((len(x),len(y)))
    for ii,i in enumerate(x):
        for jj,j in enumerate(y):
            list[ii][jj]=compute(complex(i,j),maxiter)
    return list


if __name__ == '__main__':
    xmin=-2
    xmax=0.5
    ymin=-1.25
    ymax=1.25
    width=1000
    height=1000
    maxiter=100
    t0=time.clock()
    values=mandel(xmin,xmax,ymin,ymax,width,height,maxiter)
    t1=time.clock()
    print('the time it take for numba is {:.3f}'.format(t1-t0))
    plt.imshow(values, cmap = plt.cm.gist_stern,extent = (xmin,xmax,ymin,ymax))
    plt.show()

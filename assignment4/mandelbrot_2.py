import numpy as np
import matplotlib.pyplot as plt
import time
from my_modul import *

def mandel(xmin,xmax,ymin,ymax,width,height,maxiter):
    x=np.linspace(xmin,xmax,width)
    y=np.linspace(ymin,ymax,height)
    """
      the np.ravel creates a complex number by makeing the
      x the real number and the y the imaginary one. then
      it puts them in an array.
    """
    c=np.ravel(x + y[:,None]*1j)
    c=c.reshape((width,height)) # reshape it to fit the proper dimension

    z=np.zeros((width,height)) # used as z0
    list=np.zeros((width,height))

    for i in range(maxiter):
        z=z*z + c
        isgreater=np.greater(abs(z),2.0)
        list=np.where(isgreater,i,list) 
        z=np.where(isgreater,complex(0,0),z)
        c=np.where(isgreater,complex(0,0),c)

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

    t2=time.clock()
    """
      mandel_python() is a function found in my my_modul.py.
      this helps me from rewriting of the same method.
    """
    mandel_python(xmin,xmax,ymin,ymax,width,height,maxiter)
    t3=time.clock()

    print('the time it take for numpy is {:.3f}'.format(t1-t0))
    print('the time it take for python is {:3f}'.format(t3-t2))

    plt.imshow(values, cmap = plt.cm.gist_stern,extent = (xmin,xmax,ymin,ymax))
    plt.show()

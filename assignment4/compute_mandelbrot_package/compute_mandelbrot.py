import numpy as np
import matplotlib.pyplot as plt

"""
  this compute Mandelbrot using the python way and i didn't make it
  accept argument from commandline becasues it wasn't specified so
  file_name can be inserted at the main method.
"""
def compute(c,maxiter):

    z=0
    for i in range(maxiter):
        z=z**2 + c

        if abs(z) > 2:
            return i
    return 0

def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=100,plot_filename=None):
    x=np.linspace(xmin,xmax,Nx)
    y=np.linspace(ymin,ymax,Ny)

    # creating a 2-dim array using only python
    list=[[0] * len(x) for lx in range(len(y))]

    for ii,i in enumerate(x):
        for jj,j in enumerate(y):
            list[ii][jj]=compute(complex(i,j),max_escape_time)

    # if file name is given it will plot if not it wont plot anything
    if plot_filename != None:
        myplot(xmin,xmax,ymin,ymax,list,plot_filename)
    return list

def myplot(xmin,xmax,ymin,ymax,list,file_name):
     plt.imshow(list, cmap = plt.cm.gist_stern,extent = (xmin,xmax,ymin,ymax))
     plt.savefig(file_name)
     plt.show()

if __name__ == '__main__':
    xmin=-2
    xmax=0.5
    ymin=-1.25
    ymax=1.25
    width=1000
    height=1000

    list=compute_mandelbrot(xmin,xmax,ymin,ymax,width,height,100,'my_pic')

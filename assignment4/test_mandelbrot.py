from compute_mandelbrot import compute_mandelbrot
import numpy as np



def test_mandelbrot_lessThan():
    """
     i assumed in this test that if the list contains any value in the list
     contains a value that is greater than 0, this means that some of the z
     becomes more than 2 after 0 iteration.
    """
    xmin=-2
    xmax=0.5
    ymin=-1.25
    ymax=1.25
    width=1000
    height=1000
    list=compute_mandelbrot(xmin,xmax,ymin,ymax,width,height)
    assert(np.any(list) > 0)

def test_mandelbrot_greater():
    """
     i assumed in this test that if after 0 iteration that is z=z+c becomes
     grater than abs(2), then 0 is returned since it is the first iteration.
     if all the list have the value 0 then all of them are greater than abs(2)
     at 0 iteration.
    """
    xmin=3
    xmax=4
    ymin=3
    ymax=4
    width=1000
    height=1000
    list=compute_mandelbrot(xmin,xmax,ymin,ymax,width,height)
    assert(np.all(list) == 0)

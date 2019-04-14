import math
'''
This class implements the complex class in python in a similar way
'''
class Complex():
    # parameters are the real number and the imag which is the imaginary
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    # this method helps in printng out the complex numbers
    def __str__(self):
        return '(%s + %si)' % (self.real,self.imag)
    # this method check equality of two complex number by comparing each
    # real and imaginary number of the two given complex number
    def __eq__(self,other):
        return self.real == other.real and self.imag == other.imag
    # this method conjucates a given number this is done by multipling
    # the imaginary part with -1
    def __conjucate__(self):
        self.imag=self.imag * -1
        return Complex(self.real,self.imag)
    # this method returns the modules of a given complex number.
    # the formuma is taken from the assignment text
    def __modules__(self):
        return int(math.sqrt(self.real**2 + self.imag**2))
    # adds two complex number and returns a complex number
    def __add__(self,other):
        a=self.real + other.real
        b= self.imag + other.imag
        return Complex(a,b)
    # subtracts two complex number and returns a complex number
    def __sub__(self,other):
        a=self.real - other.real
        b= self.imag - other.imag
        return Complex(a,b)
    # multipies two complex number. the method for multiping of two
    # complex number was taken from piazza
    def __mul__(self,other):
        a=(self.real * other.real) - (self.imag * other.imag)
        b=(self.real * other.real) + (self.imag * other.imag)
        return Complex(a,b)
   # this method do the same as __mul__ but it is going to be
   #used by the complex class from python

    def __rmul__(self,other):
        a=(self.real * other.real) - (self.imag * other.imag)
        b=(self.real * other.real) + (self.imag * other.imag)
        return Complex(a,b)
     # method  that is going to be used by the complex class of python
    def __radd__(self,other):
        return __add__(self,other)
     # method that is going to be used by the complex class of python
    def __rsub__(self,other):
        return __sub__(self,other)

w=Complex(5,6)
a=Complex(2,4)
c=complex(2,4)
d=complex(3,5)
print("tall1 is ",w)
print("tall2 is ",a)
print("addinng ",(w+a))
print("subtracting " ,(w-a))
print("multipling ", (w * a))
print("modules ",w.__modules__())
print("equal ",(w==a))
#print(w.__conjucate__())
print(w * c)
print((Complex(2,3) + (2+2j) )== Complex(4,5))
print((4 * Complex(3,4) - 2) == Complex(10,2))

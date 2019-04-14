from complex import Complex

'''
  this test class test the methods that are implementd in Complex
  all tests are similar. i take two Complex number add,sub,mul,eq
  them and asserts if the gets the same answr
'''

'''
test if the addition of two complex number returns the expected answer
this is the same for the __sub__ __mul__ etc
'''
def test___add__():
    z=Complex(2,4)
    w=Complex(2,4)
    assert z + w == Complex(4,8)

def test___sub__():
    z=Complex(2,4)
    w=Complex(2,4)
    assert z - w == Complex(0,0)

def test___mul__():
    z=Complex(2,4)
    w=Complex(2,4)
    assert z * w == Complex(-12,20)

def test___modules__():
    z=Complex(2,4)
    assert z.__modules__() == 4

def test__eq__():
    z=Complex(2,4)
    w=Complex(2,4)
    assert (z == w) == True

def test___conjucate__():
    z=Complex(2,4)
    assert z.__conjucate__() == Complex(2,-4)

# test the multiplication of Complex and complex class
def test___rmul__():
    z=Complex(2,4)
    w=complex(2,4)
    assert z * w == Complex(-12,20)

def test___radd__():
    z=Complex(2,4)
    w=complex(2,4)
    assert z + w == Complex(4,8)

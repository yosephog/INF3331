from distutils.core import setup
"""
  here i am assuming that my modul compute_mandelbrot is found
  in a package called compute_mandelbrot_package
"""
setup(name='Mandelbrot',
      version='1.0',
      description='calculate and plot Mandelbrot',
      packages=['compute_mandelbrot_package'],
      py_modules=['compute_mandelbrot']
     )

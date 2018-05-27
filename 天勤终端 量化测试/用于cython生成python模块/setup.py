from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name = 'y_tools',
    ext_modules=cythonize([
        Extension("y_tools", ["y_tools.py"]),
    ]),
)

"""
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(
           "rect.pyx",                 # our Cython source
           sources=["Rectangle.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
      ))
      
from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules = cythonize(Extension(
           "rect",                                # the extension name
           sources=["rect.pyx", "Rectangle.cpp"], # the Cython source and
                                                  # additional C++ source files
           language="c++",                        # generate and compile C++ code
      )))
      

      
"""
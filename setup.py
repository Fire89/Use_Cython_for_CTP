from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name = 'DyCppInterface',
    version = '1.0',
    author = 'Marcelo Salloum dos Santos',
    # The ext modules interface the cpp code with the python one:
    ext_modules=[
        Extension("cmdapi",
            sources=["cmdapi.pyx" ], # Note, you can link against a c++ library instead of including the source
            include_dirs=["./ctpapi",'.'],
            language="c++",
            library_dirs=['./ctpapi'],
            libraries=['thostmduserapi'])
    ],
    cmdclass = {'build_ext': build_ext},
)
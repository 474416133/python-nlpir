'''
setup.py file for NLPIR
'''
from distutils.core import setup, Extension
 
NLPIR_module = Extension('_NLPIR',sources=['NLPIR_wrap.cxx'], libraries = ['NLPIR'])

setup(name = 'NLPIR',
    version = '1.0',
    author = 'Killua',
    description = 'python for NLPIR',
    ext_modules = [NLPIR_module],
    py_modules = ['NLPIR'],
    )

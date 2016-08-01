# Adapted from distutils documentation

from distutils.core import setup, Extension

extension = Extension('_measurement_kit',
                      language = "c++",
                      extra_compile_args = ['-std=c++11'],
                      libraries = ['measurement_kit'],
                      sources = ['py_module.cpp'])

setup(name = 'measurement_kit',
      version = '0.3.0-dev.1',
      description = 'Portable C++11 network measurement library',
      author = 'Simone Basso',
      author_email = 'bassosimone@gmail.com',
      url = 'https://measurement-kit.github.io/',
      long_description = '''
Portable C++11 network measurement library (Python bindings)
''',
      py_modules = ["measurement_kit"],
      ext_modules = [extension]
      )

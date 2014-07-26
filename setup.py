from distutils.core import setup

setup(
    name='tehpug',
    version='1.0',
    py_modules=['tehpug'],
    install_requires=['click'],
    url='http://mehdy.net',
    license='GPLv2',
    author='mehdy',
    author_email='mehdy.khoshnoody@gmail.com',
    description='click tutorial',
    entry_points='''
    [console_scripts]
    tehpug=tehpug:main
    ''',
)

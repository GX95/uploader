from setuptools import setup

setup(
    name='upload',
    version='1.0',
    py_modules=['upload'],
    install_requires=[
        'requests',
    ],
    entry_points='''
        [console_scripts]
        upload=upload:main
    '''
)

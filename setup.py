'''
Setup Model to setup Python Handlers (model handler) for the Model plugin
'''

import setuptools

setuptools.setup(
    name='jupyterlab_model',
    version='0.1.0',
    author='Model Intern Team, sgds',
    long_description=' ',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=['notebook'],
    packages_data={'jupyterlab_model': ['.*']}
)
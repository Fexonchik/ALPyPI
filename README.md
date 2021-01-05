# ALPyPI

Warning: this is not a PyPI author's creation. If you are thinking of complaining, please send me an email : proxpro791@gmail.com.

ALPyPI (Automatic  Loading to PyPI) is a convenient and fast software for fast download of packages to PyPI.

This works according to an extremely simple scheme: at startup, setuptools and twine are installed. Next, setup.py is deployed and the package is loaded into PyPI.

# Install

You can install this, use pip or setup.py.

If pip:

###### python(3) -m pip install alpypi

if setup.py:

(Please install Git previous all this)

###### git clone https://github.com/Fexonchik/ALPyPI.git

###### cd ALPyPI

###### python(3) setup.py install

Ready? Next.

# Usage

To use this, enter the command:

###### python(3) -m alpypi

If you want to create wheel (file *.whl):

###### python(3) -m alpypi --build-wheel

Output:

###### Username:

Enter your username on PyPI and press Enter.

Next:

###### Password:

(the author does not read your data and now it is almost useless) Enter your password of this account on PyPI.

Congratulations! Your package is published on PyPI!

P.S: This replaces only two or four commands.
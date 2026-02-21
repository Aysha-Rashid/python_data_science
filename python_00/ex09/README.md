# This is a use the ft_package package

# In order to use the functions from this package, you first need to install the package

# To install the package:
# You have to be in the ex09 folder
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
# either of them will work

# In order to check if the package is installed
pip list
# you will see your package listed

# To use it just import it in your python module
from ft_package import printString 
""" 
from mymodule import divide

# import mymodule
# if you want to access everything within the other file and not specific functions.

print(divide(10, 2))
print(__name__)
# OUTPUT
# mymodule.py:  mymodule
# 5.0
# __main__

# Only the file you run is dunder main. Other files will be named according to their path.
 """
""" 
import sys
print(sys.path)
 """

import mymodule
# OUTPUT
# mymodule.py:  mymodule
# mylib.py libs.mylib

# The above output shows that __name__ outputs the path. 

import sys

print(sys.modules)
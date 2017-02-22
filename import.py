#You can import functions from another file like this
import functions

functions.print_none()
functions.print_one("Emilie")
functions.print_two("Emilie", 23)

#Name it something different
import functions as fn 

fn.print_none()
fn.print_one("Emilie")
fn.print_two("Emilie", 23)

##Just call in the functions you need
from functions import print_none, print_one, print_two

print_none()
print_one("Emilie")
print_two("Emilie", 23)

#Import all functions
from functions import *

add(20,8)
multiply(80,2)
subtract(73,4)
divide(100,2)

#Imports a file from inside a folder
#Note: You need to create an empty file called `__init__.py` in that folder
from other_folder.other_function import other_functions

other_functions()
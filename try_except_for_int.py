# The int() function takes either a number or a string. 
# It can convert the string "21" to the integer 21, but it can't convert "dog" to a number. 
# Thus, it's getting the right type, but it's still not a value that it can convert. 
# This is when we get the ValueError. It's of the right type, but the value is such that it still can't be done.

# That being said, if we tried to send in something that was neither a string nor a number, 
# it would have generated a TypeError as it is of the wrong type.


import sys

print('Please give an input.')
s = input().strip()
try:
    print(int(s))
except ValueError: # ValueError vs TypeError as above, know all kinds of exceptions, check python folder
    print('Bad String') 

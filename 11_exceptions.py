
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""



"""
Error handling in Python is done through the use of exceptions that are caught 
in try blocks and handled in except blocks. If an error is encountered, 
a try block code execution is stopped and transferred down to the except block
"""

try:
    x = int(input("please enter a number: "))
except Exception as e:
    print(e)



# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except:
#         print ("oop's thats not a valid input")


# Raise Exceptions
"""
Raise allows you to through exception at anytime
"""

x = 10
if x > 5:
    raise ValueError('x should not exceed 5. The value of x was: {}'.format(x))



# Assert Error
"""
We assert that a certain condition is met. If this condition turns out to be True, 
then that is excellent! The program can continue. If the condition turns out to be 
False, you can have the program throw an AssertionError exception
"""

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'Fancy Shoe', 'price': 400}

#25% off
apply_discount(shoes, 0.25)

#200% off
apply_discount(shoes, 2)

# User defined Exceptions
"""
Python throws errors and exceptions, when there is a code gone wrong, which may cause program to 
stop abruptly. Python also provides exception handling method with the help of try-except. Some of 
the standard exceptions which are most frequent include IndexError, ImportError, IOError, ZeroDivisionError, 
and FileNotFoundError.
"""

# Index Error
l1 = [1, 2, 3]
l1[3]

# No module named
import nomodule

# Key Error
D1 = {'a': 1, 'b':2, 'c':3}
D1['4']

# cannot import name
from math import data




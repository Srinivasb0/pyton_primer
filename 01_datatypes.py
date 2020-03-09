# printing in python
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


print("Hello World") - python 3.0
#print "Hello world" - python 2.0

# variables
"""
Variables can hold values of different data types. Python is a dynamically typed 
language hence we need not define the type of the variable while declaring it. 
The interpreter implicitly binds the value with its type.
Python enables us to check the type of the variable used in the program. 
Python provides us the type() function which returns the type of the variable passed
"""

A = "Hello"     # Data type - String
B = 10          # Data type - Int
C = 10.34       # Data type - Float
D = 10+1J       # Data type - String
E = True        # Data type - Boolean (False)

print(type(A))
print(type(B))
print(type(C))
print(type(D))
print(type(E))


# concatenation
"""
Concatenation is combining string with string or string with number or number with number

You can use either + or , to join together
If you use the "+" to join integers and floats together, then you will perform an arithmetic operation
If you use the ",", then it will print them out separately, with a space.
"""

full_name = "Robert Markov"
company_name = "Hitachi"
location = "USA"

concatenation_1 = full_name + company_name + location
concatenation_2 = full_name, company_name, location
concatenation_3 = full_name + company_name, location







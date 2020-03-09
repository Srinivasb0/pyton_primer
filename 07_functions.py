
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


"""
A function is a block of organized, reusable code that is used to perform a single, related action
The idea of a function is to assign a set of code, and possibly variables, known as parameters, 
to a single bit of text
"""

def add_number(X, Y):
    Z = X + Y
    """
    This function is
    to add multiple numbers"""
    print(Z)

add_number(1, 3)


def addme(my_list):
    my_list.append([1, 2, 3, 4])
    print("Values inside a function", my_list)
    return

my_list = [23, 25, 26, 28]
addme(my_list)


## Function Parameters
"""
The term parameter (sometimes called formal parameter) is often used to refer 
to the variable as found in the function definition, while argument (sometimes called actual parameter) 
refers to the actual input supplied at function call
The idea of function parameters in Python is to allow a programmer who is using that function, 
define variables dynamically within that function. For example:
"""

def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)
    
simple_addition(5,3)

## Keyword Arguments
"""
Keyword argumnet is the in a function call, 
the caller identifies the argument by its parameter
"""
simple_addition(num2=3,num1=5)

## Functions Parameters Defaults

"""
A default argument is an argument that assumes a default value 
if a value is not provided in the function call for that argument.
we have function parameter defaults, which allow the function's creator 
to set "default" values to the function parameters. This allows anyone to use 
a function with the default values, yet lets anyone who wishes to customize them the ability 
to specify different values.
"""
def simple(num1, num2=5):
    Pass

color = ["red", "black"]
model = ["sports", "luxury"]


def car(color, model, brand="Ferrari"):
    for c in color:
        print("color :", c)
        if c == "red":
            model1 = model[0]
            print(brand, c, model1)
        else:
            print(brand, color[1], model[1])
    print("Selecting the car")

# arbitrary arguments

def add_number(*nums):
    z = nums[0] + nums[1]
    print(z)

add_number(1, 2, 3)

# arbitrary keyword arguments

def add_number(**nums):
    z = nums['num1'] + nums['num2']
    print(z)

add_number(num1 = 1, num2 = 2, num = 3)



# Return Statement

"""
Return statement is to return from a function or to breakout a function, 
optionally it returns a value from function
A return statement with no arguments is the same as return None.
"""

def sum():
    x = 2
    y = 6
    z = x + y
    print(z)
    return z 
    
sum()

def sum_num(arg1, arg2):
    total = arg1 + arg2
    return total

sum_num(10, 20)







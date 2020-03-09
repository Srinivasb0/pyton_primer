
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


"""
Dictionaries are a data structure in Python that are very similar to associative arrays. 
They are non-ordered and contain "keys" and "values." Each key is unique and the values 
can be just about anything, but usually they are string, int, or float, or a list of these 
things. Dictionaries are defined with {} curly braces.
Use {} curly brackets to construct the dictionary, and [] square brackets to index it. 
Separate the key and value with colons : and with commas , between each pair. 
Keys must be quoted As with lists we can print out the dictionary by printing 
the reference to it. A dictionary maps a set of objects (keys) to another set of objects (values)
Dictionaries are mutable and unordered DataStructures
"""

fruit_basket = {"Apple": "Red", "Orange": "Orange", "Banana": "Yellow"}
fruit_basket['Apple'] 
fruit_basket["strawberry"] = "Red" # adding new element
del fruit_basket["strawberry"] # deleting on key


## multi dimensional Dictionary

"""
Single Key - Multiple Values
"""

fruits = {"Apple": ["Red", "round"], "Orange": ["Orange", "round"], "Banana": ["Yellow", "hook"]}
fruits["Apple"][1]

fruits = {"fruits_name":{
    "Apple":{
        "color":"red",
        "Shape": "round"
        
    },
    
    "Orange":{
        "color":"Orange",
        "Shape": "round"
    }
}}

fruits["fruits_name"]
fruits["fruits_name"]["Apple"]


## python Dictionary Comprehension

squares = {x: x**x for x in range(1,10)}
even_numbers = {x: x**x for x in range(1,10) if x%2==0}

## Builtin functions with Dictionary
"""
len() - Returns length of the dictionary
sorted() - Returns a new sorted list in dictionary
"""









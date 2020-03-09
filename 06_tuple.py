

"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""



"""
A Tuple is a dataset that similar to lists. but a tuple is fundamentally different 
in that a tuple is "immutable." This means that it cannot be changed, modified,
or manipulated. A tuple is typically used specifically because of this property.
A popular use for this is sequence unpacking, where we want to store returned data 
to some specified variables. Something like:
"""

sub = ('physics', 'chemistry', 1997, 2000)
id = (1, 2, 3, 4, 5 )
alph = ("a", "b", "c", "d")

# 'tuple' object does not support item assignment
sub[0] = 'Maths'

# 'tuple' object doesn't support item deletion
del sub[0]

## tuple packing
full_name = "satya", "nadella"

## tuple unpacking
fname, lname = full_name






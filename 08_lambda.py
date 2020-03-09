
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""



"""
The lambda operator or lambda function is a way to create small anonymous functions, 
i.e. functions without a name. These functions are throw-away functions, 
i.e. they are just needed where they have been created. Lambda functions are mainly 
used in combination with the functions map()
"""
lambda_func = (lambda x: x + 2)(2)
lambda_func = (lambda x,y: x + y)(2,3)



# map

"""
The advantage of the lambda operator can be seen when it is used in combination with 
the map() function. map() is a function with two arguments
"""

map_func = map(lambda x: x+1, [1, 2, 3, 4, 5])
print(list(map_func))

## Map with lambda function
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
map_func = map(lambda x: x['name'], dict_a)


map_func = map(lambda x: x['name']=='python', dict_a )
print(list(map_func))


## Multiple iterable to the map function

list_a = [1, 2, 3]
list_b = [10, 20, 30]

map_func = map(lambda x, y: x + y, list_a, list_b)
print(list(map_func))

# Reduce
"""
The reduce() function accepts a function and a sequence and returns
a single value calculated as follows
"""
from functools import reduce
reduce_func = reduce((lambda x, y: x+y),[2, 3, 4, 5])
reduce_func = reduce((lambda x, y: x*y),[2, 3, 4, 5])
reduce_func = reduce((lambda x, y: x%y),[2, 3, 4, 5])
print(reduce_func)

# filter
"""
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.
"""

filter_func = filter(lambda x: x > 3, [1, 2, 4, 6, 7, 4, 9])
filter_func = filter(lambda x: x % 2 == 0, [1, 2, 4, 6, 7, 4, 9])

print(list(filter_func))


filter_list = list(filter(lambda x: (x<5), [1, 2, 3, 7, 8] ))
print("The filtered lists are", filter_list)

filtered_list2 = list(filter(lambda x: (x%2==0), [1, 2, 3, 7, 8]))
print(filtered_list2)

map_list = list(map(lambda x, y, z: x*y*z, [1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(map_list)

reduce_list = reduce(lambda x, y: x * y, [1, 2, 3, 5, 6, 7])
print(reduce_list)

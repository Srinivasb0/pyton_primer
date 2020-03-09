
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""



"""
Data structures are basically the particular way of organizing data. In other words, they are used to store a collection of related data.
There are four built-in data structures in Python 
1. list 
2. tuple 
3. dictionary
4. set 
"""

# Python List
"""
A list is a data structure that holds an ordered collection of items 
i.e. you can store a sequence of items in a list,
A Python list acts very much like an array
"""


x = [1,3,5,6,2,1,6]
print(x)

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
print(sea_creatures)

## Indexing List

## positive indexing:  0 , n
"""
'Shark' : 0 
'cuttlefish' : 1
'squid' : 2
'mantis shrimp' : 3
'anemone' : 4
"""

## Negative indexing : -1 , -n

"""
'Shark' : -5 
'cuttlefish' : -4
'squid' : -3
'mantis shrimp' : -2
'anemone' : -1
"""

## Slicing list
"""
With slices, we can call multiple values by creating a range of index numbers separated by a colon
"""


print(sea_creatures[3]) 
print(sea_creatures[3])


"""
When creating a slice, as in [1:4], the first index number 
is where the slice starts (inclusive), and the second index number 
is where the slice ends (exclusive), which is why in our example above 
the items at position, 1, 2, and 3 are the items that print out
"""

print(sea_creatures[1:4])
print(sea_creatures[:3])
print(sea_creatures[2:])

print(sea_creatures[-4:-2])
print(sea_creatures[-3:])

## list manipulation

x = [1,6,3,2,6,1,2,6,7]

x.append(55) # 
x.insert(2,33) # insert based on index
del (x[2]) # delete based on index
x.remove(3) # remove the fist occurance element
x.pop(1) # remove based on index and return the value
print(len(x)) # number of elements 
x.sort() # sorting by default ascending
x.sort(reverse = True) # sorting in descending
print(x)


## Multi Dimensional List

fruits = [["Apple", "Red"], ["Orange", "Orange"], ["Banana", "Yellow"], ["Grape", "Black"]]
fruits[0]
fruits[0][1]
fruits[0][1] = "Green" # update list
del fruits[0][1] # delete based on index

print(fruits)








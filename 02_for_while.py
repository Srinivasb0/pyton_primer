
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


# While loop

"""
While loop Repeats a statement or group of statements while a given condition 
is TRUE. It tests the condition before executing the loop body.  This repeats 
until the condition/expression becomes false.
"""

number = 1
while number < 4:
    print(number)
    number += 1

## infnite loops

"""
An infinite loop (sometimes called an endless loop is a piece of coding that lacks a 
functional exit so that it repeats indefinitely
"""
# number = 1
# while number < 10:
#     print(number)

## while else loops

number = 1
while number < 5:
    print(number)
    number += 1
else:
    print("count is not lessthan 5")

# break

name = "Robert"
while name == "Robert":
    print(name)
    age = 25
    salary = 20000
    bonus = 20000*0.2
    total_salary = salary + bonus
    print(name, salary, age, bonus, total_salary)
    break


# For loop

"""
It iterates over a sequence of object and go through each item in a sequence. 
Sequence is just an ordered collection of items
For Loop, Executes a sequence of statements multiple times and abbreviates the code that 
manages the loop variable.
The next loop is the For loop. The idea of the for loop is to "iterate" through something. 
For each thing in that something, it will do a block of code. Most often, you will see a for loop's structure very much like this.
"""

exampleList = [1,5,6,6,2]

for x in exampleList:
    print(x)

for x in range(1,3):
    print(x)


for indices, x in enumerate(range(1, 4)):
    print(indices, x)

names = ["robert", "james", "mary", "rachell"]

#For loop exits after last value in list
#n is new variable to store every iterated next element

for n in names:
    print(n)
print("Every thing is fine")


## Nested For loop

for x in range(1, 3):
    for y in range(1, 3):
        print ('%d * %d = %d' % (x, y, x*y))


# Dictionary
fruit_basket = {"Apple": "Red", "Orange": "Orange", "Banana": "Yellow"}
for key, value in fruit_basket.items( ):
    print(key, value)

# break


for number in range(4):
    number = number + 1
    if number == 4:
        break
    print('number :', number)

# Continue

"""
The continue statement gives you the option to skip over the part of a 
loop where an external condition is triggered, but to go on to complete the rest
of the loop. That is, the current iteration of the loop will be disrupted, 
but the program will return to the top of the loop
"""

number = 0

for number in range(4):
    number = number + 1
    if number == 5:
        continue    # continue here
    print('Number is ' + str(number))

# print('Out of loop')

# pass
"""
When an external condition is triggered, the pass statement allows you to handle 
the condition without the loop being impacted in any way; all of the code will 
continue to be read unless a break or other statement occurs.
"""

number = 0
for number in range(6):
    number = number + 1
    if number == 5:
          pass    # pass here
    print('Number is ' + str(number))

print('Out of loop')

for i in range(10):
    # do nothing 10 times
    pass



# iteration on dictionary

fruits = {"Apple": ["Red", "round"], "Orange": ["Orange", "round"], "Banana": ["Yellow", "hook"]}

for key in fruits.keys():
    print(key)

for value in fruits.values():
    print(value)

for key, value in fruits.items():
    print(key, value)

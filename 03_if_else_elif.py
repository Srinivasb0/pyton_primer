"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""



"""
The if statement is used to check a condition: if the condition is true, we run a block of statements 
(called the if-block), else we process another block of statements (called the else-block).
"""
x = 5
y = 10

if x < y:  #True
    print('x is lesser than y')


## if elif else

x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x > z: #True
    print('x is less than z')
else:
    print('Conditions are not satisfied')


## Nested if

statement1 = True
nested_statement = True

if statement1: #False
    print("true")
    
    if nested_statement:
        print("yes")
        
    else:
        print("no")
        
else:
    print("false")






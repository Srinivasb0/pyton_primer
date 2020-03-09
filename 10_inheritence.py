
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


"""
Inheritence is a powerful feature in object oriented programming. 
It refers to define a new class with littile or no modification to an existing class

- The New Class is called Child Class
- One From which inherited is called Base or Parent Class
- This results the Re-Usability of code
"""


class Developer:
    # class variables for all instances
    
    def __init__(self, fname, lname, company):
        # instance variables unique to each instance
        self.fname = fname
        self.lname = lname
        self.email_id = fname + lname + "@" + company + ".com"
        self.company = company
        self.fullname = self.fname + self.lname

    def displayuser(self):
        return "The developer name is {} email id is {} company is {} \
         eligible for bonus {}".format(self.fullname, self.email_id, self.company, self.bonus)


class Manager(Developer):
    def __init__(self, fname, lname, company, salary):
        super().__init__(fname, lname, company)
        self.salary = salary
        self.bonus = salary * 0.2

    def total_salary(self):
        self.total_salary = self.salary + self.bonus
        return self.total_salary 


user1 = Manager("ram", "sharma", "abc", 20000)
user2 = Manager("satya", "raj", "abc", 25000)
user3 = Manager("nidhi", "mukharjee", "abc", 280000)

# user1_salary = user1.total_salary()
# user2_salary = user2.total_salary()
# user3_salary = user3.total_salary()
# print(user1_salary, user2_salary, user3_salary)


## Multiple Inheritence
class HR(Manager):
    ManagerID = '0003'
    def __init__(self, fname, lname, company, salary, approval):
        super().__init__(fname, lname, company, salary)
        self.approval = approval


    def show_details(self):
        return "{} {} {} {} {} {}".format(self.fullname, self.email_id, self.salary, self.company, self.approval, HR.ManagerID)




user1 = HR("ram", "sharma", "abc", 20000, "Yes")
user2 = HR("satya", "raj", "abc", 25000, "Yes")
user3 = HR("nidhi", "mukharjee", "abc", 280000, "Yes")

# user1_status = user1.show_details()
# print(user1_status)


# over riding the inheritence functionality

class ChangeManager(HR):
    ManagerID = '0004'

    def show_details(self):
        return "{} {} {} {} {} {}".format(self.fullname, self.email_id, self.salary, self.company, self.approval, ChangeManager.ManagerID)


user1 = ChangeManager("ram", "sharma", "abc", 20000, "Yes")
print(user1.show_details())





"""
type

Python have a built-in method called as type which generally come in handy 
while figuring out the type of variable used in the program in the runtime.
"""

print(type(user1) == dict)
print(type(user1) == ChangeManager)


"""
isinstance

"""

print(isinstance(user1, ChangeManager))
print(isinstance(Manager, Developer))



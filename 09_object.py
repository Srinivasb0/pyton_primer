
"""
Execute the below code in a cell by cell and see the output. There are Assignments to do it by your own, so complete that as well
Use the Spyder run and execute these .py files
"""


"""
Object - A unique instance of a data structure that's defined by its class. 
An object comprises both data members (class variables and instance variables) and methods.

Instance − An individual object of a certain class.

Method − A special kind of function that is defined in a class definition.
"""

# The first argument of every class method, including init, is always a reference to the current instance of the class. 
# By convention, this argument is always named self

class Developer:
    # class variables for all instances
    bonus = "Yes"
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


# creating attributes for every instance
user1 = Developer("ram", "sharma", "abc")
user2 = Developer("satya", "raj", "abc")
user3 = Developer("nidhi", "mukharjee", "abc")


# Displaying the output of the instance

instance_1 = user1.displayuser()
print(instance_1)
print(user1.fullname, user1.company, user1.email_id)







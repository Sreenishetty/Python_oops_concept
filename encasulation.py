# ENCAPSULATION --> It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
# There are 2 types of access specifiers: Private and Public


# https://pynative.com/python-encapsulation/  ---> Encapsulation in detailed


'''

Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class
Protected Member: Accessible within the class and its sub-classes

'''

class Employee:

    def __init__(self,name,salary):
        self.name = name            #Public Member(accessible within/outside the a class)
        
        self._project = project     #Protected Member(accessbile within the class and its sub-classes)

        self.__salary = salary      #Private Member(accessbile only within a class)



'''
Public Member

Public data members are accessible within and outside of a class. All member variables of the class are by default public.

'''

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print("Name: ", emp.name, 'Salary:', emp.salary)

# calling public method of the class
emp.show()



'''
Private Member

We can protect variables in the class by marking them private. To define a private variable add two underscores as a prefix at the start of a variable name.

Private members are accessible only within the class, and we can’t access them directly from the class objects.

'''

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing private data members
print('Salary:', emp.__salary)

# AttributeError: 'Employee' object has no attribute '__salary'


'''
In the above example, the salary is a private variable. As you know, we can’t access the private variable from the outside of that class.

We can access private members from outside of a class using the following two approaches

Create public method to access private members
Use name mangling
Let’s see each one by one

'''

'''
Public method to access private members
Example: Access Private member outside of a class using an instance method

'''

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()



'''
Name Mangling to access private members
We can directly access private and protected variables from outside of a class through name mangling. The name mangling is created on an identifier by adding two leading underscores and one trailing underscore, like this _classname__dataMember, where classname is the current class, and data member is the private variable name.

Example: Access private member

'''
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)



'''
Protected Member
Protected members are accessible within the class and also available to its sub-classes. To define a protected member, prefix the member name with a single underscore _.

Protected data members are used when you implement inheritance and want to allow data members access to only child classes.

'''

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)














































# class car:
#     def __init__(self):
#         self.__updatesoftware() 
#         """Two underscores are been used before the method name,so it is a private method"""

#     def drive(self):
#         print("I'm Driving")

#     def __updatesoftware(self):
#         print("Software Updating")
#         """we can't access/modify the private method outside the class"""

# blackcar = car()
# blackcar.drive()


# # class car:
# #     __maxspeed = 0
# #     __name = ''
# #     def __init__(self):
# #         self.__maxspeed = 200
# #         self.__name = "Supercar"
    
# #     def drive(self):
# #         print("I'm Driving")
# #         print(self.__maxspeed)

# #     def setspeed(self,speed):
# #         self.__maxspeed = speed
# #         print(self.__maxspeed)

# # redcar = car()
# # redcar.drive()
# # redcar.setspeed(100)


# # redcar.__maxspeed = 100
# # redcar.drive()
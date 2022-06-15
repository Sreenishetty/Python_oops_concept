# CLASS AND OBJECTS
# Python OOP
# class Student:
#     pass

# stu1 = Student()
# stu2 = Student()

# # Instance Variables

# stu1.name  = "Ram"          
# stu1.rollno = 100
# stu1.dob = 1993

# stu2.name = "anand"
# stu2.rollno = 200
# stu2.dob = 1996

# print(stu1.name)
# print(stu2.rollno)



from datetime import date

class Person:
    def __init__(self, name , dob, city):
        self.name = name  
        self.dob = dob
        self.city = city

    def age(self):
        return date.today().year - self.dob

class Student(Person):
    # __init__ is a dunder/ magic method..
    # when a object is created this methd is called automaticaly
    # self refers to the current object
    #  name , rollno, dob, city is a local variables 
    # converting the local variables to instance variables we use self.name methods
    fees = 10000
    no_of_stu = 0
    def __init__(self, name , rollno, dob, city):
        # self.name = name
        super().__init__(name, dob, city)
        self. rollno = rollno       
        # self.dob = dob
        # self.city = city
        Student.no_of_stu = Student.no_of_stu + 1
    # the above are the attributes

    # def address(self):
    #     address = f"Name : {self.name}\nDOB : {self.dob}\
    #             \nRollno : {self.rollno}\nCity : {self.city}"
    #     return address

    def age(self):
        # current_year = date.today().year
        # return current_year - self.dob
        return date.today().year - self.dob
    # to hold the object of the class we have declared the self parameter
    # if it is not declared this gives a typerror
    # Student.age(stu1) in this way the oject is called, Hence stud1 has no value,
    # bcz of that it throws an error..... self is a mandatory

    # def pay_fees(self,amount):
    #     self.fees = self.fees - amount
        # in instance mtd frst argument is passed as object

    # @classmethod
    # def change_fees(cls, amount):
    #     cls.fees = amount 
        # to change the class variable value we use cls method
        # cls.fees is also written as Student.fees
        #  in class mtd frst argument is passed as cls
    # @classmethod
    # def stu_data(cls,data):
    #     name, rollno, dob, city = data.split(",")
    #     return cls(name, rollno, dob, city)

    # @staticmethod
    # def department(dept):
    #     avilable_dept = ['mechnical','cs']
    #     if dept in avilable_dept:
    #         return True
    #     return False
        # in static mtd there will be no frst arguments such as cls and object
         
class Mechanical(Student):
    fees = 12000
    """This type of changing the value in the child class is known as mtd overridding"""
    def __init__(self, name , rollno, dob, city,year):
        super().__init__(name, rollno, dob, city)
        self.year = year
        # super is a inbuilt function which is used to access te mtds of the parent/base class
        # SINGLE INHERITANCE
# stu1 = Student("ram",100,1998,"Blore")
# stu2 = Student("Ravan",200,1993,"M  ysore")

class Teacher(Person):
    def __init__(self, name , dob, city, students = []):
        super().__init__(name, dob, city)
        self.students = students

    def show_students(self):
        for student in self.students:
            print(student.name)



stu1 = Mechanical("ram",100,1998,"Blore",2021)
stu2 = Mechanical("Ravan",200,1993,"Mysore",2022)

t1 = Teacher('walker',1989,"chennai",[stu1,stu2])
# print(stu1.name)
# print(stu2.city)

# # print(stu1.address())
# # print(stu2.address())

# # print(stu1.age())
# # print(stu2.age())


#         # CLASS VARIABLES
# # Instance variables
# # stu1.fees = 10000
# # stu2.fees = 10000

# # stu1.fees = 20000
# # print(stu1.__dict__)
# # stu1.pay_fees(5000)

# # print(Student.fees)
# # print(stu1.fees)
# # print(stu2.fees)

# # class variables
# # Student.fees = 20000
# # print(Student.fees)

# # print(stu1.no_of_stu)
# # print(stu2.no_of_stu)
# # print(Student.no_of_stu)



# CLASS METHOD, STATIC METHOD AND INSTANCE METHOD

# INSTANCE MTD is the normal mtd which is declared like address and age

# Student.change_fees(120000)
# print(stu1.fees)
# print(stu2.fees)
# data = 'sam,300,1997,salem'
# stu3 = Student.stu_data(data)
# print(stu3.name)

# print(stu1.department('cs'))

# INHERITANCE

# print(dir(stu1))
# print(stu1.age())
# print(Mechanical.__mro__) 
"""method resolution order"""
# This __mro__ is used to check how thw child class(Mechanical) is working
# or the flow of child class--> first it checks in the Mech class and then in Student cls and the object of it
# print(stu1.name)
# print(stu1.age())

# multiple inheritance --> calling different class name in a single class 
# multi-level inheritance --> person --> Student --> Mechanical
# hierarchical inheritance --> person class is used thrice in Student class and also in Teacher class
# this type of heritance is called as  hierarchical inheritance

print(t1.name)
# print(t1.age())
t1.show_students()
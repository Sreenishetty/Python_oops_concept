from datetime import date

class Student():
    fees = 10000
    no_of_stu = 0
    def __init__(self, name , rollno, dob, city):
        self.name = name
        self. rollno = rollno       
        self.dob = dob
        self.city = city
        Student.no_of_stu = Student.no_of_stu + 1
        
    def age(self):
        return date.today().year - self.dob


class Mechanical(Student):
    fees = 12000
    """This type of changing the value in the child class is known as attribute overriding"""
    def __init__(self, name , rollno, dob, city,year):
        super().__init__(name, rollno, dob, city)
        self.year = year

    def display(self):
        print("Method belongs to class Mechanical")

stu1 = Mechanical("ram",100,1998,"Blore",2018)
stu2 = Mechanical("Ravan",200,1993,"Mysore",2021)


stu1 = Student("ram",100,1998,"Blore")
stu2 = Student("Ravan",200,1993,"Mysore")

# print(dir(stu1))
# print(stu1.age())
# print(Mechanical.__mro__) 
# print(stu1.name)

# print(stu1.age())
print(stu1.name)
# print(stu1.year)

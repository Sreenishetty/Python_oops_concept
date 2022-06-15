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

    def address(self):
        address = f"Name : {self.name}\nDOB : {self.dob}\
                \nRollno : {self.rollno}\nCity : {self.city}"
        return address

    def age(self):
        current_year = date.today().year
        return current_year - self.dob

    def pay_fees(self,amount):
        self.fees = self.fees - amount

stu1 = Student("ram",100,1998,"Blore")
stu2 = Student("Ravan",200,1993,"Mysore")

# # Instance variables
# stu1.fees = 10000
# stu2.fees = 10000

# stu1.fees = 20000
# print(stu1.__dict__)
# stu1.pay_fees(5000)

# print(Student.fees)
# print(stu1.fees)
# print(stu2.fees)

# class variables
Student.fees = 20000
# print(Student.fees)

print(stu1.no_of_stu)
print(stu2.no_of_stu)
print(Student.no_of_stu)
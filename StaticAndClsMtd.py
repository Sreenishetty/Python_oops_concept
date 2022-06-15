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

    def pay_fees(self,amount):
        self.fees = self.fees - amount

    @classmethod
    def change_fees(cls, amount):
        cls.fees = amount 
        # to change the class variable value we use cls method
        # cls.fees is also written as Student.fees
        #  in class mtd frst argument is passed as cls
    @classmethod
    def stu_data(cls,data):
        name, rollno, dob, city = data.split(",")
        return cls(name, rollno, dob, city)

    @staticmethod
    def department(dept):
        avilable_dept = ['mechanical','cs']
        if dept in avilable_dept:
            return True
        return False
        # in static mtd there will be no frst arguments such as cls and object
         
stu1 = Student("ram",100,1998,"Blore")
stu2 = Student("Ravan",200,1993,"Mysore")


# Student.change_fees(12000)
# print(stu1.fees)
# print(stu2.fees)

# data = 'sam,300,1997,salem'
# stu3 = Student.stu_data(data)
# print(stu3.name)

# print(stu1.department('mechanical'))
# print(stu1.department('cs'))
# print(stu1.department('civil'))
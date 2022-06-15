from datetime import date

class Person:
    def __init__(self, name , dob, city):
        self.name = name  
        self.dob = dob
        self.city = city

    def age(self):
        return date.today().year - self.dob

class Student(Person):
    fees = 10000
    no_of_stu = 0
    def __init__(self, name , rollno, dob, city):
        super().__init__(name, dob, city)
        self. rollno = rollno       
        Student.no_of_stu = Student.no_of_stu + 1
        
    def age(self):
        return date.today().year - self.dob

class Mechanical(Student):
    fees = 12000
    def __init__(self, name , rollno, dob, city,year):
        super().__init__(name, rollno, dob, city)
        self.year = year

class Teacher(Person):
    def __init__(self, name , dob, city, students = []):
        super().__init__(name, dob, city)
        self.students = students
    
    def show_students(self):
        for students in self.students:
            print(students.age())

class College(Teacher, Student):
    pass

stu1 = Mechanical("ram",100,1998,"Blore",2018)
stu2 = Mechanical("Ravan",200,1993,"Mysore",2021)
# print(stu1.name)
# print(stu1.age())


t1 = Teacher('walker',1985,'salem', [stu1,stu2])
print(t1.name)
# print(t1.age())
t1.show_students()

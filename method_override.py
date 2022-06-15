#   METHOD OVERRIDING

class A:
    def display(self):
        print("Method belongs to class A")

class B(A):
    # pass
    def display(self):
        print("Method belongs to class B")

b1 = A()
b1.display()
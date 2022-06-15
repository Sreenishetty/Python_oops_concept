# POLYMORPHISM and MTD OVERRIDDING
# POLY --> MANY
# MORPHISM --> BEHAVIOUR

class version1:

    def button(self):
        print("Colour RED")


class version2(version1):

    def button(self):
        print("Colour BLUE")

a = version1()
a.button()
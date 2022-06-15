#  METHOD OVERLOADING

# first product method
# takes two args and print their product
def product(a,b):
    p = a * b
    print(p)

# Second product method
# takes three args and print their product
def product(a,b,c):
    p = a * b * c
    print(p)

# uncommenting the above line shows an error
product(4,5)

# This line will call the second product method
product(5, 9, 1)



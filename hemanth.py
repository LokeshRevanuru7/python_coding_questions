# DEFINING A FUNCTION:-
""""
        def greet():
            print("hello, welcome to python")
        greet()

"""

# FUNCTION WITH PARAMETER:-
"""
def add(a,b):
    return a + b

result  = add(5,6)
print(result)
"""

# FUNCTION ARGUMENTS:-

# 1. Position Arguments:-

"""
def full_name(first, last):
         print(f"FULL NAME:{first} {last}")

full_name("revanuru", "lokesh")
"""

# 2. default arguments:-
"""
def greet(name="guest")
    print(f"Hello, {name}!")

greet()
greet("loka")
"""

# 3. keyword arguments:-
"""
def student_details(name, age, course):
    print(f"Name: {name}, Age:{age}, Course:{course}")

student_details(name="loka", age=26, course="python")
"""

# 4. Arbitary Arguments:-(args, *kwargs)
# Allows passing args(multiple position arguments)
"""
def sum_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum:{total}")

sum_numbers(1,2,3,4,5,6)
"""

# **kwargs()
# Allow passing multiple keyword arguments as a dictionary

"""
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="vasantha", age=24, city="chennai")
"""

# returning values form functions
"""
def square(num):
    return num*num

result = square(6)
print(result)
"""

# returning multiple values

"""
def calculate (a,b):
    return a+b, a-b, a*b, a/b

add, sub, mul, div = calculate(10,5)
print(add, sub, mul, div)

o/p:- 15, 5, 50, 2.0
"""

# scopes and lifrtime of varaibles.

# local scope:- varaibles defined inside a function exit only withn that function

# global scope:- varaibles defined outside all functions can be accessed anywhere.

"""
x=10

def my_function():
    x=5 
    print("inside function:", x)

my_function()
print("outside function:", x)
"""

# recursive functions

# factorial using recursive

"""
def factorial(n):
    if n==0:
        return 1 
    return n * factorial(n-1)

print(factorial(5))
"""

# fibonaaci series using recursive

"""
def fibonaaci(n):
    if n<=0:
        return 0
    elif n ==1:
        return 1 
    else:
        return fibonaaci(n-1) + fibonaaci(n-2)
print(fibonaaci(6))
"""

# Anonymous(lambda) function:-

# lambda function
"""
square = lambda x:x*x
print(square(5))
"""

# lambda function with multiple arguments
"""
add = lambda a,b: a+b
print(add(3,4)) 
"""

# using lambda with map(), filter(), reduce()

# 1. map() function
# Applies a function to all elements in an iterable
"""
numbers = [1,2,3,4,5]
sqared_numbers = list(map(lambda x:x**2, numbers))
print(sqared_numbers)
"""

# 2. filter() function
# filter elements based on condition
"""

numbers = [10, 20, 30, 40, 50, 21, 45]
odd_numbers = list(filter(lambda X:X%2!=0, numbers))
print(odd_numbers)
"""

# reduce() function(requires functools)
# performs cumlative operations

""""
from functools import reduce
numbers = [1,2,3,4,5]
sum_all = reduce(lambda a,b: a+b, numbers)
print(sum_all)
"""







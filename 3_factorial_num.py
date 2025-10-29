# factorial of a num
#ex:- 5! = 5*4*3*2*1 = 120

# inbuilt
import  math
num =5
fact = math.factorial(num)
print(fact)
# or
print(f"factorial of {num} is {fact}")


# for loop
num = 6
fact = 1
for i in range(1, num+1):
    fact *= i

print(f"factorial of {num} is {fact}")

# list comprehension
import math
num = 7
fact = math.prod([i for i in range(1,num+1)])
print(f"factorial of {num} is {fact}")



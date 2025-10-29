# swapping with or without using 3rd variable

#with 3rd variable
a =5
b =10
print("before swapping a=", a)
print("before swapping b=", b)
temp = a
a= b
b =temp

print("after swapping a=",a)
print("before swapping b=", b)

print("=====")
#without 3rd variable
a = 15
b = 20
a,b = b,a
print("a=", a)
print("b=", b)

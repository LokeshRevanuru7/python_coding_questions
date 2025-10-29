# reverse a string 3 ways

# inbuilt way

string1= "lokesh"
reverse = string1[::-1]
print(reverse)

# using for loop
string1= "lokesh"
Reverse = ""
for i in string1:
    Reverse = i + Reverse

print(Reverse)

#list comprehension
string1= "lokesh"
revverse = ''.join([string1[i] for i in range(len(string1)-1, -1, -1)])
print(revverse)



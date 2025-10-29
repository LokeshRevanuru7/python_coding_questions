#find missing number in list

# inbuilt
numbers = [1,2,3,4,6,7,8,9,10]
n=10
full_set = set(range(1,n+1))
missing = list(full_set - set(numbers))
print(missing[0])


# for loop
n= 10
missing = None
for i in range(1, n+1):
    if i not in numbers:
        missing = i
        break
print(missing)



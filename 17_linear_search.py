# linear search

# inbuilt:- using keyword & index()
numbers = [10,23,45,70,11,15,67]
target  =70
if target in numbers:
    index = numbers.index(target)
    print(f"{target} found at index number {index}")
else:
    print(f"{target} not found in the list")

# for loop
numbers = [10,23,45,70,11,15,67]
target  =20
found = False

for i in range(len(numbers)):
    if numbers[i]  == target:
        found = True
        print(f"{target} found at index{i}")
        break

if not found:
    print(f"{target} not found in the list")

#   ascending to descending order list


# inbuilt:-
numbers = [5,2,9,0,1,3,4]
asc = sorted(numbers)
dsc = sorted(numbers)

print(asc)
print(dsc)


# for loop
numbers1 = [5,2,9,0,1,3,4]


#Ascending order
for i in range(len(numbers1)):
    for j in range(0, len(numbers1) -i-1):
        if numbers1[j] > numbers1[j+1]:
            numbers1[j] , numbers1[j+1] = numbers1[j+1], numbers1[j]

print("Ascen", numbers1)


#descending order
for i in range(len(numbers1)):
    for j in range(0, len(numbers1) -i-1):
        if numbers1[j] < numbers1[j+1]:
            numbers1[j] , numbers1[j+1] = numbers1[j+1], numbers1[j]

print("Desend", numbers1)

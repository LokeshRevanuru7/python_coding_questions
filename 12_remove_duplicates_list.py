#  remove duplicates in list

#inbuilt
numbers = [1,2,3,3,2,4,5,1,3]
unique_list = list(set(numbers))
print(unique_list)


#for loop
numbers1 = [1,2,3,3,2,4,5,1,3,6,7]
unique_list = []
for num in numbers1:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)
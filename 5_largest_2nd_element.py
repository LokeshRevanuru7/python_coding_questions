# largest and 2nd largest element in list


# inbuilt

numbers = [10,45,23,78,56,89,13]
sorted_list = sorted(numbers)
second_largest = sorted_list[-2]
print(second_largest)


# using bubble sort
l = [2, 4, 44, 23, 54, 26,101]
def get_second_large(l):
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l[-2]

print(get_second_large(l))


# with loop
number = [2, 4, 44, 23, 54, 26,101,24,55]
largest = second_largest = float('-inf')
for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("second largest",second_largest)


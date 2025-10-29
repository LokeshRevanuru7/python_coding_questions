# binary search

#inbuilt

import bisect
from os import MFD_ALLOW_SEALING

numbers = [10,20,30,40,50,60,70,70,90,100]
target = 70

index = bisect.bisect_left(numbers,target)
if index < len(numbers) and numbers[index] == target:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in the list")



# for loop

# here order should be in ascending order
numbers1 = [10,20,25,30,40,50,60,70,70,90,100,110]
target = 110
low =0
high  = len(numbers1) -1
found = False

while low <= high:
    mid = (low + high)//2
    if numbers1[mid] == target:
        found = True
        print(f"{target} found at index {mid}")
        break
    elif numbers1[mid] < target:
        low = mid + 1
    else:
        high = mid -1
if not found:
    print(f"{target} not found in the list")

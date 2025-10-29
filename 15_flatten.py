# flatten

#inbuilt:-
from itertools import chain
nested_list = [[1,2], [3,4,5], [6,7],[8,9]]

flatten_list = list(chain.from_iterable(nested_list))
print(flatten_list)

# forloop:-
nested_list1 = [[1,2], [3,4,5], [6,7],[8,9],[10]]
flatten_list = []

for sublist in nested_list1:
    for item in sublist:
        flatten_list.append(item)
print(flatten_list)
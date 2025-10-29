# sort dictionary by keys

#inbuilt:-
my_dict = {'b':3, 'a':1, 'd':4, 'c':5}
sorted_dict = {key:my_dict[key] for key in sorted(my_dict)}
print(sorted_dict)

#for loop
my_dict = {'b':5, 'e':2, 'a':1, 'c':3, 'd':4}
sorted_keys = list(my_dict.keys())
sorted_keys.sort()
sorted_dict = {}

for key in sorted_keys:
    sorted_dict[key] = my_dict[key]
print(sorted_dict)

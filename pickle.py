pickle module is used to serializing and deserializing python objects
    converts to python object to byte stream

# 1 save:- serialize an object

import pickle
data = {'name': 'lokesh', 'age': 25, 'skills': ['python', 'automation']}

# write to binary file
with open('data.pk1', 'wb') as file:
    pickle.dump(data,file)

print("data saved sucesssfully")


# 2 load:- deserialize an object
import pickle

with open("data.pl1", 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

# o/p:-
{'name': 'lokesh', 'age':25, 'skills':['python','automation']}





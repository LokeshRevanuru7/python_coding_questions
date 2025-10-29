# json -> javascript object notation  , lightweight, easy to read/write,
#  it's easy for machines to parse and generate


# methods
# 1. json.dumps()  :- convert to object to json string
# 2. json.dump()   :- write python object as json to file
# 3. json.loads()  :- convert json string to python object
# 4. json.load()   :- read json from a file not python object


#1. json.dumps() :- convert to object to json string (serialization)

# using dumps 

import json
data = {
    "name" : "Lokesh",
    "age" : 26,
    "skills" : ["python", "automation", "react"],
    "is_active" : True
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

#2. json.dump()   :- write python object as json to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)


# 3 reading json from a file
with open("data.json" "r")as f:
    data_from_file = json.load(f)


#4 read json from a file not python object (deserialization)

json_str = '{"name : "Lokesh, "age": 25, "skills":["python", "automation"], "is_active": true}'

#convert json string to python dict
data_dict = json.loads(json_str)
print(data_dict)
print(type(data_dict))


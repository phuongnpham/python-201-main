# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

dict = {}

for key in dict_1:
    dict[key] = dict_1[key]

for key in dict_2:
    if key in dict:
        dict[key] = dict_1[key] + dict_2[key]
    else:
        dict[key] = dict_2[key]

print(dict)
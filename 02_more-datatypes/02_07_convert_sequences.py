# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
tuple_string = tuple(string)
print(tuple_string)
list_string = list(tuple_string)
print(list_string)
list_string[0] = "k"
final_tuple = tuple(list_string)
print(final_tuple)
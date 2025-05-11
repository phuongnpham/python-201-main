'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

#function to get the number value of the tuple
def get_value(tup):
    return tup[1]
#use sorted method to sort the list
sorted_list = sorted(unsorted_list, key=get_value)
print(sorted_list)
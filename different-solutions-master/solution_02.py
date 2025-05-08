'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []
#loop through the unsorted list 
for tuple_ in unsorted_list:
    #add the value of the tuple in a list
    value_list.append(tuple_[1])

print(value_list)
#sorted the value list
value_list.sort()
#loop through the sorted value list
for value in value_list:
    #loop through the unsorted list
    for tuple_ in unsorted_list:
        #if tuple value equal the value in value list
        if tuple_[1] == value:
            #add the tuple in sorted list
            sorted_list.append(tuple_)
            #remove the tuple in unsorted list
            unsorted_list.remove(tuple_)
            break

print(sorted_list)

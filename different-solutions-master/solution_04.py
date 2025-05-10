'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#loop through the unsorted list
for tup in list(unsorted_list):
    #current min is the value of the first tuple
    current_min = unsorted_list[0][1]
    index = 0
    #loop through the length of unsorted list to find the min value
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])
#display the unsorted list, not necessary since the list is empty
print(unsorted_list)
print(sorted_list)

'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []
#loop through the length of unsorted list
for x in range(0, len(unsorted_list)):
    #assign the value of the first tuple to min
    min = unsorted_list[0][1]
    #display min value, not necessary
    print(min)
    index = 0

    for i in range(0, len(unsorted_list)):
        #if the current value less than min then assign that value to min
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            #index equal current position
            index = i
    #add the current tuple to sorted list
    sorted_list.append(unsorted_list[index])
    #remove the current tuple from unsorted list
    unsorted_list.remove(unsorted_list[index])

#display the unsorted list, not necessary since the list is empty
print(unsorted_list)
print(sorted_list)

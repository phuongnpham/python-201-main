# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [num for items in starter_list for num in items]
print(flattened_list)

# Flatten a list of any depth
starter_list = [[1, 2, 3, 4], [[5, 6]], [[[7, 8, 9]]]]
flattened_list = []
while starter_list: # run until the given list is empty
    item = starter_list.pop()
    # print(item)
    if type(item) == list: # check the type of the poped item
        starter_list.extend(item) # if list extend the item to given list
        # print(starter_list)
        # print(flattened_list)
    else:
        flattened_list.append(item) # if not list then add it to the flat list
        # print(starter_list)
        # print(flattened_list)
flattened_list.sort()
print(flattened_list)

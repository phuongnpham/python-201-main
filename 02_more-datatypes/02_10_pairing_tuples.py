# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)
pair_list = []
# Write your code below here
sorted_list = sorted(randlist)
print(sorted_list)
for i in range(0, len(sorted_list), 2):
    if len(sorted_list) - i == 1:
        pair_list.append((sorted_list[i], 0))
    else:
        pair_list.append((sorted_list[i], sorted_list[i+1]))
for pair in pair_list:
    print(pair)
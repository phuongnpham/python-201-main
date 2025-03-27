# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# Method 1:
duplicates_removed_list = set(list_)
print(duplicates_removed_list)

# Method 2:
duplicates_removed_list = []
for i in list_:
    if i not in duplicates_removed_list:
        duplicates_removed_list.append(i)
print(duplicates_removed_list)
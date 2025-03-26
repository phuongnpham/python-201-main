# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

string = input("Please enter a string: ")
split_string = string.split()
word_count = {}
for i in split_string:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(max(word_count, key=word_count.get))
# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
with open("03_file-input-output/words.txt", "r") as file_in:
    word = file_in.readlines()
word_reversed = word[::-1]
with open("03_file-input-output/words_reverse.txt", "w") as file_out:
    file_out.writelines(word_reversed)

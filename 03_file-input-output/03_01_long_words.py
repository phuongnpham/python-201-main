# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

with open("03_file-input-output/words.txt", "r") as file_in:
    for word in file_in:
        word = word.strip()
        if len(word) > 20:
            print(word)
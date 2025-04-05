# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

word_dict = {}
total_words = 0
with open("03_file-input-output/words.txt", "r") as file_in:
    for word in file_in:
        total_words += 1
        word = word.strip()
        word_dict.update({word: len(word)})

shortest_word = min(word_dict.values())
longest_word = max(word_dict.values())
for word in word_dict.keys():
    if len(word) == shortest_word:
        print(f"Shortest word: {word}")
for word in word_dict.keys():
    if len(word) == longest_word:
        print(f"Longest word: {word}")
print(f"Total number of words in file: {total_words}")
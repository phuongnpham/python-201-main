user_input = input("Please enter a sentence: ")
count_dict = {
    "upper": 0,
    "lower": 0,
    "punctuation": 0,
    "total": 0
}
for char in user_input:
    if char.isspace():
        continue
    else:
        count_dict["total"] += 1
        if char.isupper():
            count_dict["upper"] += 1
        elif char.islower():
            count_dict["lower"] += 1
        else:
            count_dict["punctuation"] += 1

print(f'Upper case: {count_dict["upper"]}')
print(f'Lower case: {count_dict["lower"]}')
print(f'Punctuation: {count_dict["punctuation"]}')
print(f'Total chars: {count_dict["total"]}')
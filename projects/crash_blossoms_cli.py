def title_case(text):
    title_case = []
    for word in text.split():
        cap_word = word.capitalize()
        title_case.append(cap_word)
    return " ".join(title_case)

user_input = input("Enter your sentence (type exit to quit): ")
while user_input.lower() != "exit":
    crash_blossom = title_case(user_input)
    print(crash_blossom)
    user_input = input("Enter your sentence (type exit to quit): ")
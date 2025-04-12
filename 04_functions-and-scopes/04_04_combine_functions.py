# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    return f"Hello {name}!"

def write_letter(name, text):
    greeting = greet(name) + "\n\n"
    good_bye = f"\n\nBest, \n{name}"
    letter = greeting + text + good_bye
    return letter

name = "John"
text = "How's it going? Let's catch up soon"
letter = write_letter(name, text)
print(letter)
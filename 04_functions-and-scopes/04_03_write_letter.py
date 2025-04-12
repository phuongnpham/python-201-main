# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.
def write_letter(name, text):
    greeting = f"Dear {name},\n\n"
    goodbye = f"\n\nBest regards,\n{name}"
    letter = greeting + text + goodbye
    return letter

name = "John"
text = "Hope you're doing well"
letter = write_letter(name, text)
print(letter)
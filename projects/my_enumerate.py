# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable):
    """Mimic the built-in enumerate() function

    Args:
        iterable: Any iterable input (e.g. list, tuple)
    """
    index = 0
    result = []
    for value in iterable:
        result.append((index, value))
        index += 1
    return result

courses = ['Intro', 'Intermediate', 'Advanced', 'Professional']

for index, course in my_enumerate(courses):
    print(f"{index}: {course} Python")
# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.
def make_sandwich(bread, *toppings):
    """Creat a sandwich with the bread on top and bottom, and the toppings in between.

    Args:
        bread (str): The type of bread for the sandwich.
        *toppings: An arbitrary amount of toppings.

    Returns:
        str: A string representing the sandwich with the bread on top and bottom, and the toppings in between.
    """
    sandwich = [bread]
    sandwich.extend(toppings)
    sandwich.append(bread)
    return "\n".join(sandwich)

print(make_sandwich("wheat", "lettuce", "tomato", "ham"))
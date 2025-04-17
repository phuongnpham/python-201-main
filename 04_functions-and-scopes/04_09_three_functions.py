# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
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

def customize_sandwich(bread, topping_list):
    valid_topping = [t for t in topping_list if t.strip()]
    sandwich = make_sandwich(bread, *valid_topping)
    return sandwich

def order_summary(bread, toppings, customer_name):
    sandwich = customize_sandwich(bread, toppings)
    summary = f"Order for: {customer_name}\n"
    summary += f"Sandwich:\n{sandwich}\n"
    return summary

bread = "white bread"
toppings = ["ham", "cheese", "lettuce", "tomato"]
customer_name = "Alice"
print(order_summary(bread, toppings, customer_name))
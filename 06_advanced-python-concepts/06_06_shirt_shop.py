# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cartesian_product = [(color, size) for color in colors for size in sizes]

print("Welcome to TShirt Online Shop!")
print("*" * 50)

for index, (color,size) in enumerate(cartesian_product, start=1):
    product_name = f"{color.title()} T-Shirt. Size {size}"
    print(f"{index}. {product_name}")
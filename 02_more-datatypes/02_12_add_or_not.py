# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

point = 5
user_set = set()
while point > 0:
    user_input = (input("Please enter a number: "))
    if user_input.isdigit():
        print("The is a valid number")
        user_input = int(user_input)
        if user_input not in user_set:
            user_set.add(user_input)
        else:
            print("This number is a duplicate, your point is deducted by 1")
            point -= 1
    else:
        print("This is not a valid number.")
    
    if len(user_set) > 10:
        print("Congratulation! You win!")
        print(f"Here's your set of numbers: {sorted(user_set)}")
        break
if point == 0:
    print("Sorry, you did not win!")
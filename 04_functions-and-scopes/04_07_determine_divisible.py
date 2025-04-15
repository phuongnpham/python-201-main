# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages
def is_divisible_by_4_or_7(number):
    """Check if the number is divisible by 4 OR 7

    Args:
        number (int): the number to check

    Returns:
        boolean: True if divisible by 4 OR 7, otherwise False
    """
    return number % 4 == 0 or number % 7 == 9

def is_divisible_by_4_and_7(number):
    """Check if the number is divisible by 4 AND 7

    Args:
        number (int): the number to check

    Returns:
        boolean: True if divisible by 4 AND 7, otherwise False
    """
    return number % 4 == 0 and number % 7 == 0

user_input = int(input("Please enter a number between 1 and 1,000,000,000: "))

if 1 <= user_input <= 1000000000:
    or_check = is_divisible_by_4_or_7(user_input)
    and_check = is_divisible_by_4_and_7(user_input)

    print(f"Is {user_input} divisible by 4 or 7? {or_check}")
    print(f"Is {user_input} divisible by 4 and 7? {and_check}")
else:
    print("Number must be in between 1 and 1,000,000,000")
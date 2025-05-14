# Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on 
# what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. 
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

import random

valid_choices = {"1", "2"}
inventory = []

player_name = input("Please enter your name: ")
print(f"Welcome {player_name} to our adventure!")
print("There are two doors in front of you, left door and right door.")
print("""What's your choice?
1. Left door
2. Right door""")
first_choice = input(" ")

while first_choice not in valid_choices:
    first_choice = input("Please enter 1 for left door or 2 for right door: ")

if first_choice == "1":
    print("This is a blacksmith room. You see a sword.")
    print("""Do you want to:
    1. Take the sword
    2. Leave it""")
    sword_choice = input(" ")

    while sword_choice not in valid_choices:
        sword_choice = input("Please enter 1 or 2: ")

    if sword_choice == "1":
        inventory.append("sword")
        print("You picked up the sword.")
    else:
        print("You left the sword.")

    print("You're now back in the previous room and open the right door.")
    print("Oh no! You encounter a dragon!")

if first_choice == "2" or first_choice == "1":
    if "sword" in inventory:
        print("You have a sword to fight the dragon!")
        player_strength = random.randint(5, 10)
        dragon_strength = random.randint(1, 10)
        print(f"Your strength: {player_strength}, Dragon's strength: {dragon_strength}")

        if player_strength >= dragon_strength:
            print("You slay the dragon! You win!")
        else:
            print("The dragon overpowers you. You lose your inventory.")
            inventory.clear()
    else:
        print("You are unarmed and get eaten by the dragon.")

print("""Do you want to:
1. Explore further
2. End the game""")
next_choice = input(" ")

while next_choice not in valid_choices:
    next_choice = input("Please enter 1 or 2: ")

if next_choice == "1":
    print("You explore deeper and find a shield.")
    inventory.append("shield")
    print(f"You pick up the shield. Current inventory: {inventory}")
    print("You walk into a new room and encounter a bandit!")

    if "sword" in inventory:
        player_strength = random.randint(4, 10)
    else:
        player_strength = random.randint(1, 5)

    bandit_strength = random.randint(3, 8)
    print(f"Your strength: {player_strength}, Bandit's strength: {bandit_strength}")

    if player_strength >= bandit_strength:
        print("You defeat the bandit!")
    else:
        print("The bandit defeats you and steals your items.")
        inventory.clear()

else:
    print("Thanks for playing!")

print(f"Game over. Your final inventory: {inventory}")

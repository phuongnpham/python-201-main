import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    hands = {0: "scissor", 1: "rock", 2: "paper"}
    # for example if the variable hand is 0, it should return the string "scissor"
    return hands.get(hand)

def determine_winner(player_hand, computer_hand):
    if player_hand == computer_hand:
        return "It's a tie"
    elif (player_hand == 0 and computer_hand == 2) or \
         (player_hand == 1 and computer_hand == 0) or \
         (player_hand == 2 and computer_hand == 1):
        return "Player wins"
    else:
        return "Computer wins"

def main():
    user_continue = "y"
    while user_continue.lower() == "y":
        player_choice = int(input("Please enter your choice (0 = scissor, 1 = rock, 2 = paper): "))
        while player_choice not in range(0, 3):
            player_choice = int(input("Invalid choice! Please enter 0, 1 or 2: "))
        computer_choice = random.randint(0, 2)
        player_hand = get_hand(player_choice)
        computer_hand = get_hand(computer_choice)
        print(f"Player hand: {player_hand}")
        print(f"Computer hand: {computer_hand}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        user_continue = input("Do you want to continue? (y/n): ")

if __name__ == "__main__":
    main()
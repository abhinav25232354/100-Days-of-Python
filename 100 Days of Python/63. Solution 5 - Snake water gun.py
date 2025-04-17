import random

# Mapping choices
choices = {"snake": 50, "water": 25, "gun": 100}
result_map = {-1: "Lose", 0: "Draw", 1: "Win"}

print("-1: Lose\n0: Draw\n1: Win")

# User input
user_choice = input("Enter your choice (snake/water/gun): ").strip().lower()

if user_choice not in choices:
    print("Invalid choice! Please enter snake, water, or gun.")
else:
    # Computer's random choice
    comp_choice = random.choice(list(choices.keys()))
    print(f"Computer chose: {comp_choice}")

    # Game rules
    if user_choice == comp_choice:
        result = 0  # Draw
    elif (user_choice == "snake" and comp_choice == "water") or \
         (user_choice == "water" and comp_choice == "gun") or \
         (user_choice == "gun" and comp_choice == "snake"):
        result = 1  # Win
    else:
        result = -1  # Lose

    print(f"You {result_map[result]}!")

from characters import Character, Stranger
from inventory import Inventory
from scenes import basement, attic, continue_game

characters = {
    "Jessica": Character("Jessica"),
    "Mike": Character("Mike"),
}

inventory = Inventory()
stranger_introduced = False

def start_game():
    print("You and your friends find yourselves in a dark, abandoned cabin.")
    print("Do you want to explore the basement or the attic first?")
    choice = input("Type 'basement' or 'attic': ").lower()

    if choice == 'basement':
        basement(characters, inventory)
    elif choice == 'attic':
        attic(characters, inventory)
    else:
        print("Invalid choice, please try again.")
        start_game()

# Start the game
start_game()

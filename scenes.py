from characters import Character, Stranger
from game_logic import change_approval, encounter_danger, find_flashlight, find_gun, find_key

def basement(characters, inventory):
    print("\nYou carefully descend into the dark, damp basement.")
    print("You see a shadowy figure in the corner and a door leading to another room.")
    print("Do you want to approach the figure or enter the room?")
    choice = input("Type 'figure' or 'room': ").lower()

    if choice == 'figure':
        change_approval(characters, "Jessica", 10)
        change_approval(characters, "Mike", -10)
        encounter_danger(characters, "ghost", inventory.has_item("flashlight"))
    elif choice == 'room':
        change_approval(characters, "Mike", 5)
        print("\nYou enter the room and find Emily hiding there. She joins your group.")
        characters["Emily"] = Character("Emily")
        hidden_room(characters, inventory)
    else:
        print("Invalid choice, please try again.")
        basement(characters, inventory)

def attic(characters, inventory):
    print("\nYou climb up the creaky stairs to the attic.")
    print("You find an old chest and a window overlooking the forest.")
    print("Do you want to open the chest or look out the window?")
    choice = input("Type 'chest' or 'window': ").lower()

    if choice == 'chest':
        change_approval(characters, "Mike", -10)
        change_approval(characters, "Jessica", 10)
        encounter_danger(characters, "cursed artifact", inventory.has_item("flashlight"))
    elif choice == 'window':
        change_approval(characters, "Jessica", 5)
        window(characters, inventory)
    else:
        print("Invalid choice, please try again.")
        attic(characters, inventory)

def hidden_room(characters, inventory):
    print("\nYou enter the hidden room and find an old diary and a strange key.")
    print("Do you want to read the diary, take the key, or search the room?")
    choice = input("Type 'diary', 'key', or 'search': ").lower()

    if choice == 'diary':
        change_approval(characters, "Jessica", 10)
        change_approval(characters, "Mike", -5)
        encounter_danger(characters, "madness from diary", inventory.has_item("flashlight"))
    elif choice == 'key':
        change_approval(characters, "Mike", 5)
        if "Emily" in characters:
            change_approval(characters, "Emily", 10)
        inventory.add_item("key")
        print("\nThe key unlocks a secret passage leading to another part of the cabin.")
        continue_game(characters, inventory)
    elif choice == 'search':
        change_approval(characters, "Mike", 5)
        change_approval(characters, "Jessica", 5)
        inventory.add_item("flashlight")
    else:
        print("Invalid choice, please try again.")
        hidden_room(characters, inventory)

def window(characters, inventory):
    print("\nYou look out the window and see a figure standing in the forest, watching you.")
    print("Do you want to signal for help or hide in the attic?")
    choice = input("Type 'signal' or 'hide': ").lower()

    if choice == 'signal':
        change_approval(characters, "Mike", 10)
        change_approval(characters, "Jessica", 5)
        if "Emily" in characters:
            change_approval(characters, "Emily", 5)
        print("\nThe figure approaches the cabin and reveals themselves to be a rescuer.")
        meet_rescuer(characters, inventory)
    elif choice == 'hide':
        change_approval(characters, "Jessica", 5)
        encounter_danger(characters, "found while hiding", inventory.has_item("flashlight"))
    else:
        print("Invalid choice, please try again.")
        window(characters, inventory)

def meet_rescuer(characters, inventory):
    print("\nThe rescuer helps you escape the cabin, but your journey isn't over yet.")
    print("You must now navigate through the dangerous forest.")
    forest_path(characters, inventory)

def forest_path(characters, inventory):
    print("\nYou find yourself on a narrow path through the forest.")
    print("Do you want to follow the path or venture into the woods?")
    choice = input("Type 'path' or 'woods': ").lower()

    if choice == 'path':
        print("\nYou follow the path and encounter a fork. Do you want to go left or right?")
        fork_in_path(characters, inventory)
    elif choice == 'woods':
        change_approval(characters, "Jessica", -5)
        change_approval(characters, "Mike", 5)
        print("\nYou venture into the woods and find an abandoned campsite.")
        abandoned_campsite(characters, inventory)
    else:
        print("Invalid choice, please try again.")
        forest_path(characters, inventory)

def fork_in_path(characters, inventory):
    choice = input("Type 'left' or 'right': ").lower()

    if choice == 'left':
        change_approval(characters, "Mike", 10)
        change_approval(characters, "Jessica", -5)
        print("\nYou encounter The Stranger who offers to help guide you.")
        meet_stranger(characters, inventory)
    elif choice == 'right':
        change_approval(characters, "Jessica", 5)
        change_approval(characters, "Mike", -5)
        print("\nYou find a small cabin where Samantha is hiding. She joins your group and gives you a gun.")
        characters["Samantha"] = Character("Samantha")
        inventory.add_item("gun")
    else:
        print("Invalid choice, please try again.")
        fork_in_path(characters, inventory)

def abandoned_campsite(characters, inventory):
    print("\nAt the campsite, you find some supplies and a map.")
    print("Do you want to take the supplies or study the map?")
    choice = input("Type 'supplies' or 'map': ").lower()

    if choice == 'supplies':
        change_approval(characters, "Mike", 10)
        change_approval(characters, "Jessica", -5)
        print("\nYou take the supplies and continue your journey.")
        continue_game(characters, inventory)
    elif choice == 'map':
        change_approval(characters, "Jessica", 10)
        change_approval(characters, "Mike", -5)
        print("\nYou study the map and find a safer route through the forest.")
        continue_game(characters, inventory)
    else:
        print("Invalid choice, please try again.")
        abandoned_campsite(characters, inventory)

def meet_stranger(characters, inventory):
    print("\nYou meet a mysterious stranger who offers to guide you.")
    characters["The Stranger"] = Stranger("The Stranger")
    
    for i in range(3):
        print("\nThe Stranger asks you a question.")
        question = input("Do you trust me? Type 'yes' or 'no': ").lower()
        if question == 'yes':
            change_approval(characters, "The Stranger", 10)
        elif question == 'no':
            change_approval(characters, "The Stranger", -10)
        else:
            print("Invalid choice, please try again.")
    
    if characters["The Stranger"].approval > 0:
        print("\nThe Stranger decides to help you further.")
        continue_game(characters, inventory)
    else:
        print("\nThe Stranger reveals his true nature and attacks you!")
        encounter_danger(characters, "stranger attack", inventory.has_item("gun"))

def continue_game(characters, inventory):
    alive_characters = len(characters)
    if alive_characters == 3:
        print("\nWith your companions, you feel more confident but must remain cautious.")
    elif alive_characters == 2:
        print("Without your lost companion, every choice now carries more weight.")
    else:
        print("With only one companion left, you must be extremely careful.")

    if "Emily" in characters and "Samantha" not in characters:
        print("Emily suggests heading to the library for more clues.")
        hidden_room(characters, inventory)
    elif "Samantha" not in characters:
        print("You hear noises from another part of the forest. Do you want to investigate or try to find another exit?")
        choice = input("Type 'investigate' or 'exit': ").lower()
        if choice == 'investigate':
            forest_path(characters, inventory)
        elif choice == 'exit':
            print("You manage to escape the cabin safely. You win!")
        else:
            print("Invalid choice, please try again.")
            continue_game(characters, inventory)
    else:
        print("You find a way to navigate through the dangers and survive the night. You win!")

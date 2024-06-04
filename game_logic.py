from characters import Character, Stranger

def change_approval(characters, character_name, amount):
    if character_name in characters:
        characters[character_name].change_approval(amount)

def encounter_danger(characters, danger_type, has_flashlight):
    willing_sacrifices = [char for char in characters.values() if char.is_willing_to_sacrifice()]
    potential_betrayers = [char for char in characters.values() if char.might_sacrifice_player()]

    if willing_sacrifices:
        sacrifice = willing_sacrifices[0]
        print(f"\nYou encounter a {danger_type}, but {sacrifice.name} sacrifices themselves to save you. You survive!")
        del characters[sacrifice.name]
    elif potential_betrayers:
        betrayer = potential_betrayers[0]
        print(f"\nYou encounter a {danger_type}, but {betrayer.name} sacrifices you to save themselves. You lose!")
    else:
        print(f"\nYou encounter a {danger_type}. Do you want to use the flashlight to spot the danger or run?")
        choice = input("Type 'flashlight' or 'run': ").lower()

        if choice == 'flashlight' and has_flashlight:
            print(f"\nYou use the flashlight to spot the {danger_type} and avoid it. You survive!")
        elif choice == 'run':
            print(f"\nYou run away from the {danger_type} and manage to escape. You survive!")
        else:
            print(f"\nYou encounter a {danger_type} and without anyone to help or a weapon, you don't survive. You lose!")
            exit(0)

def find_flashlight():
    print("\nYou find a flashlight in the hidden room. This will help you spot dangers and unlock new options.")
    return True

def find_gun():
    print("\nYou investigate the noise and find Samantha. She joins your group and gives you a gun.")
    return True

def find_key():
    print("\nYou find a strange key. This might unlock something important later.")
    return True

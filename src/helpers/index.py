def confirm_user_choice(choice: str):
    while True:
        user_response = input(f"\nYou chose '{choice}', is this correct? y/n ")
        if user_response == "y":
            return True
        elif user_response == "n":
            return False
        else:
            print("\nSelect either 'y' (yes) or 'n' (no)")
            continue


def set_user_name():
    user_name = input("Choose your username: ").capitalize()
    print(f"\nHello, {user_name}")


def set_user_class():
    while True:
        user_class = input("\nChoose your class [Mage,Warrior]: ").lower()
        if user_class == "mage" or user_class == "warrior":
            print(f"\nYou have selected {user_class}")
            user_confirmation = confirm_user_choice(user_class)
            if user_confirmation == True:
                return user_class
            else:
                continue
        else:
            print(
                f"\n{user_class.capitalize()} is not valid. Please select either mage or warrior."
            )
            continue


def addValues(x, y):
    return x + y

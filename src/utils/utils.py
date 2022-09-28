from typing import Iterable, Optional


def confirm_user_choice(choice: str, responses: Optional[Iterable[str]] = None):
    """used to confirm a user's choice"""
    if responses is None:
        # An infinite stream of calls to input()
        responses = iter(
            lambda: input(f"\nYou chose '{choice}', is this correct? y/n "), None
        )

    for user_response in responses:
        if user_response == "y":
            return True
        elif user_response == "n":
            return False
        else:
            print("\nSelect either 'y' (yes) or 'n' (no)")
    else:
        # Note: cannot be raised from the default value of responses
        raise ValueError("Unexpected end of responses")


def set_user_name():
    user_name = input("Choose your username: ").capitalize()
    print(f"\nHello, {user_name}")
    return user_name


def set_user_class():
    """returns a class for the character"""
    while True:
        user_class = input("\nChoose your class [Mage,Warrior]: ").lower()
        if user_class == "mage" or user_class == "warrior":
            print(f"\nYou have selected {user_class}")
            user_confirmation = confirm_user_choice(user_class)
            if user_confirmation == True:
                return user_class
        else:
            print(
                f"\n{user_class.capitalize()} is not valid. Please select either mage or warrior."
            )

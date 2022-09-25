class Character:
    def __init__(
        self,
        name: str,
        stats_mana: int,
        stats_armor: int,
        stats_health: int,
        stats_luck: int,
    ) -> None:
        self.name = name
        self.stats_health = stats_health
        self.stats_mana = stats_mana
        self.stats_armor = stats_armor
        self.stats_luck = stats_luck


class Mage:
    def __init__(self, type: str) -> None:
        self.type = type

    def set_type(self):
        """set's the mage's type"""
        # if type === fire
        # if type === water
        # if type === earth
        # else restart and express types


class FireMage:
    def __init__(self) -> None:
        pass

    def cast_fireball(self, username: str):
        print(f"{username} casts fireball")


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


set_user_name()
set_user_class()

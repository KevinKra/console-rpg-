from typing import List, Type
from utils.utils import set_user_name, set_user_class


class Player:
    """Player class defines and modifies Player attributes"""

    # class attributes
    allPlayers: List["Player"] = []

    def __init__(
        self,
        name: str,
    ):
        # instance attributes
        self.name = name
        self.hero_type = None
        self.stats = {"health": 100, "mana": 0, "dodge": 0, "fortune": 0}
        self.attributes = {"strength": 0, "intellect": 0, "agility": 0, "luck": 0}

        # on instance init, add self to class attribute
        Player.allPlayers.append(self)

    # magic methods
    def __repr__(self) -> str:
        return f"Player({self.name})"

    # # example of class method
    # @classmethod
    # def some_class_method(cls) -> None:
    #     """example of class method"""

    # # example of a static method
    # @staticmethod
    # def is_integer(num: int) -> bool:
    #     """checks if argument is an integer"""
    #     return isinstance(num, int)

    # instance methods
    def increase_attribute(self, selected_attribute: str) -> bool:
        """assigns attributes points"""
        if selected_attribute in self.attributes:
            self.attributes[selected_attribute] += 1
            if selected_attribute == "strength":
                self.stats["health"] += 10
            if selected_attribute == "intellect":
                self.stats["mana"] += 10
            return True
        else:
            print("\n=== Notice: ATTRIBUTE NOT FOUND ===")
            return False

    def set_player_attributes(self, attribute_points: int) -> None:
        """set stats with a set total pool of available attribute_points"""
        assert attribute_points > 0, "attribute_points must be a positive int"
        while attribute_points > 0:
            self.print_user_stats()
            self.print_attribute_allowance(attribute_points)
            selected_attribute = input()
            resolved = self.increase_attribute(selected_attribute)
            if resolved:
                attribute_points -= 1

    def print_user_stats(self) -> None:
        """prints user's current stats to console"""
        print(f"\n=== Player {self.name}'s current stats ===")
        print(f"-- Health: {self.stats.get('health')}, Mana: {self.stats.get('mana')}")
        print("-- Attributes:")
        for item in self.attributes.items():
            print(f"{item[0]}: {item[1]}")

    def print_attribute_allowance(self, attribute_points: int) -> None:
        """prints user's available attributes"""
        print(
            f"""
        You have ({attribute_points}) attribute points available, assign them to continue.
        ~to assign a value, type the name of the attribute.
        """
        )


class Game:
    """Class used to initiate and run the game."""

    def __init__(self) -> None:
        self.player = Type[Player]

    def create_player(self) -> None:
        """initializes the player"""
        user_name = set_user_name()
        set_user_class()
        self.player = Player(user_name)
        print(Player.allPlayers)
        self.player.set_player_attributes(5)

    def start_game(self) -> None:
        """root function that starts the game"""
        self.create_player()


# player = Player("tom")
# player.set_initial_player_stats()
game = Game()
game.start_game()

# ETC

# class Mage:
#     def __init__(self, type: str) -> None:
#         self.type = type

#     def set_type(self):
#         """set's the mage's type"""
#         # if type === fire
#         # if type === water
#         # if type === earth
#         # else restart and express types


# class FireMage:
#     def __init__(self) -> None:
#         pass

#     def cast_fireball(self, username: str):
#         print(f"{username} casts fireball")

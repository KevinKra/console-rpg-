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

    # instance methods
    def print_user_stats(self) -> None:
        """prints user's current stats to console"""
        print(f"\n=== Player {self.name}'s current stats ===")
        print(f"-- Health: {self.stats.get('health')}, Mana: {self.stats.get('mana')}")
        print("-- Attributes:")
        for item in self.attributes.items():
            print(f"{item[0]}: {item[1]}")

    def increase_attribute(self, selected_attribute: str) -> None:
        """increases a selected stat"""
        if selected_attribute not in self.attributes.keys():
            print("=== Notice: attribute not found")
        else:
            self.attributes[selected_attribute] += 1
            if selected_attribute == "strength":
                self.stats["health"] += 10
            if selected_attribute == "intellect":
                self.stats["mana"] += 10

    def set_player_attributes(self, attribute_points: int) -> None:
        """set stats with a set total pool of available attribute_points"""
        assert attribute_points > 0, "attribute_points must be a positive int"
        while attribute_points > 0:
            self.print_user_stats()
            selected_attribute = input(
                f"""
                You have ({attribute_points}) attribute points available, assign them to continue.
                ~to assign a value, type the name of the attribute.
                """
            )
            self.increase_attribute(selected_attribute)
            attribute_points -= 1


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

from typing import Any, List, Type


class Player:
    """Player class defines and modifies Player attributes"""

    # class attributes
    allPlayers: List["Player"] = []

    def __init__(
        self,
        name: str,
    ):
        # instance attributes
        self._name = name
        self.__hero_type = str
        self.stats = {"health": 100, "mana": 0, "dodge": 0, "fortune": 0}
        self.attributes = {"strength": 0, "intellect": 0, "agility": 0, "luck": 0}
        self.spendable_attribute_points = 0

        # on instance init, add self to class attribute
        Player.allPlayers.append(self)

    # magic methods
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name})"

    @property
    def hero_type(self) -> Type[str]:
        """gets private hero_type attribute"""
        return self.__hero_type

    @hero_type.setter
    def hero_type(self, value: Any) -> None:
        """sets private hero_type attribute"""
        self.__hero_type = value

    # instance methods
    def set_attribute_points(self, attribute_points: int) -> None:
        """sets player spendable attribute points"""
        assert attribute_points > 0, "attribute_points must be a positive int"
        self.spendable_attribute_points = attribute_points

    def spend_player_attributes(self) -> None:
        """set stats with a set total pool of available attribute_points"""
        while self.spendable_attribute_points > 0:
            self.__print_user_stats()
            self.__print_attribute_allowance()
            self.__increase_attribute()

    # private instance methods
    def __increase_attribute(self) -> None:
        """assigns attributes points"""
        selected_attribute = input()
        if selected_attribute in self.attributes:
            self.spendable_attribute_points -= 1
            self.attributes[selected_attribute] += 1
            if selected_attribute == "strength":
                self.stats["health"] += 10
            if selected_attribute == "intellect":
                self.stats["mana"] += 10
        else:
            print("\n=== Notice: ATTRIBUTE NOT FOUND ===")

    def __print_user_stats(self) -> None:
        """prints user's current stats to console"""
        print(f"\n=== Player {self._name}'s current stats ===")
        print(f"-- Health: {self.stats.get('health')}, Mana: {self.stats.get('mana')}")
        print("-- Attributes:")
        for item in self.attributes.items():
            print(f"{item[0]}: {item[1]}")

    def __print_attribute_allowance(self) -> None:
        """prints user's available attributes"""
        print(
            f"""
        You have ({self.spendable_attribute_points}) attribute points available, assign them to continue.
        ~to assign a value, type the name of the attribute.
        """
        )


# # example of class method
# @classmethod
# def some_class_method(cls) -> None:
#     """example of class method"""

# # example of a static method
# @staticmethod
# def is_integer(num: int) -> bool:
#     """checks if argument is an integer"""
#     return isinstance(num, int)

# read-only attribute
# self._name

# private attribute (only accessible within defined class)
# self.__name


# @property
# # property decorator == read-only attribute (getter)
# def name(self):
#     # additional code can go here
#     return self.__name


# @name.setter
# # setter
# def name(self, value):
#     # additional code can go here
#     self.__name = value

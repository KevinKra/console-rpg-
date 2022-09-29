"""module doc string"""


class Round:
    """simulates a round in the game"""

    def __init__(self) -> None:
        pass

    def generate_round(self) -> None:
        """test"""
        return self.__determine_random_event()

    def __determine_random_event(self) -> None:
        """sets an event"""
        self.__event_monster_encounter()

    def __event_monster_encounter(self) -> None:
        input("You encounter a monster, what do you do?")

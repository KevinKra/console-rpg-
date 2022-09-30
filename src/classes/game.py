from typing import Type
from classes.player import Player
from classes.round import Round
from utils.utils import set_user_name, set_user_class


class Game:
    """Class used to initiate and run the game."""

    def __init__(self) -> None:
        self.player = Type[Player]
        self.story_length = 0

    def __create_player(self) -> None:
        """initializes the player"""
        user_name = set_user_name()
        set_user_class()
        self.player = Player(user_name)
        self.player.set_attribute_points(3)
        self.player.spend_player_attributes()

    def __set_story_length(self) -> None:
        """set the length of the game (story)"""
        response = input("Choose a story length [short, medium, long]\n")
        while response.lower() not in ["short", "medium", "long"]:
            response = input("Enter either: short, medium, or long\n")
        if response == "short":
            self.story_length = 10
        elif response == "medium":
            self.story_length = 25
        elif response == "long":
            self.story_length = 50
        else:
            raise ValueError("Unexpected user response")

    def __initialize_game(self) -> None:
        """runner for the game"""

        game_round = Round()
        while self.story_length > 0:
            if self.story_length > 0:
                game_round.generate_round()
                self.story_length -= 1
            else:
                print("Game Complete. Stats ...")

    def start_game(self) -> None:
        """root function that starts the game"""
        self.__create_player()
        self.__set_story_length()
        self.__initialize_game()

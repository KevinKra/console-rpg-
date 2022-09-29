from typing import Type
from classes.player import Player
from utils.utils import set_user_name, set_user_class


class Game:
    """Class used to initiate and run the game."""

    def __init__(self) -> None:
        self.player = Type[Player]
        self.story_length = 0

    def create_player(self) -> None:
        """initializes the player"""
        user_name = set_user_name()
        set_user_class()
        self.player = Player(user_name)
        self.player.set_attribute_points(5)
        self.player.spend_player_attributes()

    def set_story_length(self) -> None:
        """set the length of the game (story)"""
        response = input("Choose a story length [short, medium, long]")
        while response.lower() not in ["short", "medium", "long"]:
            response = input("Enter either: short, medium, or long")
        if response == "short":
            self.story_length = 10
        elif response == "medium":
            self.story_length = 25
        elif response == "long":
            self.story_length = 50
        else:
            raise ValueError("Unexpected user response")

    def start_game(self) -> None:
        """root function that starts the game"""
        self.create_player()
        self.set_story_length()

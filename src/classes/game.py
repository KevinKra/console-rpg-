from typing import Type
from classes.player import Player
from utils.utils import set_user_name, set_user_class


class Game:
    """Class used to initiate and run the game."""

    def __init__(self) -> None:
        self.player = Type[Player]

    def create_player(self) -> None:
        """initializes the player"""
        user_name = set_user_name()
        set_user_class()
        self.player = Player(user_name)
        self.player.set_attribute_points(5)
        self.player.spend_player_attributes()

    def start_game(self) -> None:
        """root function that starts the game"""
        self.create_player()

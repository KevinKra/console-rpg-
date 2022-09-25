from utils.index import set_user_name, set_user_class


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


set_user_name()
set_user_class()

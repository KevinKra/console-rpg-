from utils.utils import set_user_name, set_user_class


class Player:
    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
        self.heroType = None
        self.health = 100
        self.mana = 0
        self.stats = {"strength": 0, "intellect": 0, "agility": 0, "luck": 0}

    def print_user_stats(self):
        """prints user's current stats to console"""
        print(f"\n=== Player {self.name}'s current stats ===")
        print(f"-- Health: {self.health}, Mana: {self.mana}")
        print(f"-- Attributes:")
        for item in self.stats.items():
            print(f"{item[0]}: {item[1]}")

    def increase_stat(self, selected_stat: str):
        """increases a selected state (optional)"""
        if selected_stat not in self.stats.keys():
            print("=== Notice: attribute not found")
        else:
            self.stats[selected_stat] += 1

    def set_player_stats(self, stat_points: int):
        """initial"""
        while stat_points > 0:
            self.print_user_stats()
            selected_stat = input(
                f"""
                You have ({stat_points}) attribute points available, assign them to continue.
                ~to assign a value, type the name of the attribute.
                """
            )
            self.increase_stat(selected_stat)
            stat_points -= 1


class Game:
    def __init__(self):
        self.player = None

    def create_player(self):
        user_name = set_user_name()
        user_class = set_user_class()
        self.player = Player(user_name)
        self.player.set_player_stats(10)

    def start_game(self):
        self.create_player()


# player = Player("tom")
# player.set_initial_player_stats()
game = Game()
game.start_game()

### ETC

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

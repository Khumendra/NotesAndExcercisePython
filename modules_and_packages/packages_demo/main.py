# import game.characters.player
# game.characters.player.get_player_info()


# from game.characters import player, boss

# player.get_player_info()
# boss.get_boss_info()
import pandas as pd
print("I am from pandas:",pd)

from game.characters.player import get_player_info
from game.characters.boss import get_boss_info

get_player_info()
get_boss_info()
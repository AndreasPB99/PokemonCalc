import math
from typing import Tuple, Optional

from src.pokemon import Pokemon
from src.move import Move
from src.type import Type, normal, dragon, fire
from src.weather import Weather


def get_type_modifier(move_type: Type, def_types: Tuple[Type, Optional[Type]]):
    bonus = 1
    for def_type in def_types:
        if def_type is None:
            continue
        bonus *= move_type.value[str(def_type)]
    return bonus


def get_weather_modifier(move_type: Type, weather) -> float:
    return 1


# https://bulbapedia.bulbagarden.net/wiki/Damage
def attack(attacker: Pokemon, defender: Pokemon, move: Move, my_random_val: int = 100, crit: int = 1, burn: bool = False, weather: Weather = Weather.NOWEATHER) -> int:
    if move.special:
        attack = attacker.stats.special_attack
        defense = defender.stats.special_defense

    else:
        attack = attacker.stats.attack
        defense = defender.stats.defense

    target_multipier = 1 # 0.75 if the move has more than one target when the move is executed
    parental_bond = 1 # 0.25 if the secnd strike of parental bond
    glaive_rush = 1 # 2 if the target used the move Glaive_rush in the previous turn

    type_effectiveness = get_type_modifier(move.type, defender.type)
    weather = get_weather_modifier(move.type, weather)
    stab = 1.5 if move.type in attacker.type else 1
    random_val = my_random_val / 100
    burn = 0.5 if burn else 1
    other = 1

    p1 = ((2 * attacker.level) / 5) + 2
    p2 = attack / defense
    damage = math.floor(((p1 * move.power * p2) / 50) + 2)

    damage_final = damage * target_multipier * parental_bond * weather * glaive_rush * crit * random_val * stab * type_effectiveness * burn * other
    return math.floor(damage_final)

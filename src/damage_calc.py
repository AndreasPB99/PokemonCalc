import math
from typing import Tuple, Optional

from src.pokemon import Pokemon
from src.move import Move
from src.type import Type, normal, dragon, fire


def get_type_effectiveness(move_type: Type, def_types: Tuple[Type, Optional[Type]]):
    bonus = 1
    for def_type in def_types:
        if def_type is None:
            continue
        bonus *= move_type.value[str(def_type)]
    return bonus


# https://bulbapedia.bulbagarden.net/wiki/Damage
def attack(attacker: Pokemon, defender: Pokemon, move: Move, my_random_val: int = 100) -> int:
    if move.special:
        attack = attacker.stats.special_attack
        defense = defender.stats.special_defense

    else:
        attack = attacker.stats.attack
        defense = defender.stats.defense

    type_effectiveness = get_type_effectiveness(move.type, defender.type)
    stab = 1.5 if move.type in attacker.type else 1
    target_multipier = 1 # 0.75 if the move has more than one target when the move is executed
    parental_bond = 1 # 0.25 if the secnd strike of parental bond
    weather = 1
    glaive_rush = 1 # 2 if the target used the move Glaive_rush in the previous turn
    crit = 1 # 1.5 if crit
    random_val = my_random_val / 100
    burn = 1 # 0.5 if burned
    other = 1
    p1 = ((2 * attacker.level) / 5) + 2
    p2 = attack / defense
    damage = math.floor(((p1 * move.power * p2) / 50) + 2)

    damage_final = damage * target_multipier * parental_bond * weather * glaive_rush * crit * random_val * stab * type_effectiveness * burn * other
    return math.floor(damage_final)

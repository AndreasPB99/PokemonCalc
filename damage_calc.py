from pokemon import Pokemon
from move import Move


def attack(attacker: Pokemon, defender: Pokemon, move: Move) -> int:
    if move.special:
        attack_power = attacker.stats.special_attack + move.power
        defense = defender.stats.special_defense + move.power

    else:
        attack_power = attacker.stats.attack + move.power
        defense = defender.stats.defense + move.power

    if defense >= attack_power:
        return 1
    return attack_power - defense
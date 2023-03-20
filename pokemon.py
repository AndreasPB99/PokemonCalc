from dataclasses import dataclass
from abc import ABC
from move import Move
from ability import *
from type import Type
from typing import Tuple, Optional

@dataclass
class Stats:
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int

    def total(self):
        return self.hp + self.attack + self.defense + self.special_attack + self.special_defense +  self.speed


@dataclass
class Pokemon:
    id: int
    type: Tuple[Type, Optional[Type]]
    stats: Stats
    moves: list[Move]
    level: int
    ability: Ability
    # TODO EV/IV

    def __post_init__(self):
        if len(self.moves) > 4:
            raise Exception('To many moves')
        elif len(self.moves) < 1:
            raise Exception('To few moves')



from dataclasses import dataclass
from player import Player
from terrain import Terrain



@dataclass
class Round:
    number: int


@dataclass
class Game:
    player1: Player
    player2: Player
    rounds: list[Round]
    terrain: Terrain
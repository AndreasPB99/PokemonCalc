from dataclasses import dataclass
from pokemon import Pokemon

@dataclass
class Player:
    pokemon: list[Pokemon]
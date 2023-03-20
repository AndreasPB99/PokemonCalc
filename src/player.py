from dataclasses import dataclass
from src.pokemon import Pokemon

@dataclass
class Player:
    pokemon: list[Pokemon]
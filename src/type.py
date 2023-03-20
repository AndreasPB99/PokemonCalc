from enum import Enum

normal = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'grass': 1,
    'electric': 1,
    'ice': 1,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,
    'bug': 1,
    'rock': 0.5,
    'ghost': 0,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1,
}

fire = {
    'normal': 1,
    'fire': 0.5,
    'water': 0.5,
    'grass': 2,
    'electric': 1,
    'ice': 2,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,
    'bug': 2,
    'rock': 0.5,
    'ghost': 1,
    'dragon': 0.5,
    'dark': 0.5,
    'steel': 2,
    'fairy': 1,
}

dragon = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'grass': 1,
    'electric': 1,
    'ice': 1,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,
    'bug': 1,
    'rock': 1,
    'ghost': 1,
    'dragon': 2,
    'dark': 1,
    'steel': 0.5,
    'fairy': 0,
}


class Type(Enum):
    NORMAL = normal
    FIRE = fire
    DRAGON = dragon
    FAIRY = 3
    WATER = 5
    GRASS = 6
    ELECTRIC = 7
    ROCK = 8
    GROUND = 9
    STEEL = 10
    BUG = 11
    PSYCHIC = 12
    DARK = 13
    GHOST = 14

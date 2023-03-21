from src.damage_calc import *
from src.pokemon import Pokemon, Stats
from src.type import Type
from src.move import *
from src.ability import Nothing as abilityNothing

fire_move = Move(Type.FIRE, 100, 1, False)
tackle = Move(type=Type.NORMAL, power=40, hits=1, special=False)
nothing_poke = Pokemon(1, (Type.NOTHING, None), Stats(205, 205, 205, 205, 205, 205), [tackle], 100, abilityNothing)
normal_poke = Pokemon(2, (Type.NORMAL, None), Stats(205, 205, 205, 205, 205, 205), [tackle], 100, abilityNothing)
fire_poke = Pokemon(3, (Type.FIRE, None), Stats(205, 205, 205, 205, 205, 205), [fire_move], 100, abilityNothing)
ghost_poke = Pokemon(4, (Type.GHOST, None), Stats(205, 205, 205, 205, 205, 205), [tackle], 100, abilityNothing)
rock_poke = Pokemon(5, (Type.ROCK, None), Stats(205, 205, 205, 205, 205, 205), [tackle], 100, abilityNothing)
grass_poke = Pokemon(6, (Type.GRASS, None), Stats(205, 205, 205, 205, 205, 205), [tackle], 100, abilityNothing)


def test_nothing():
    assert attack(nothing_poke, normal_poke, tackle) == 35


def test_normal_stab():
    assert attack(normal_poke, normal_poke, tackle) == 52


def test_normal_stab_not_very_effective():
    assert attack(normal_poke, rock_poke, tackle) == 26


def test_normal_against_ghost():
    assert attack(normal_poke, ghost_poke, tackle) == 0


def test_fire_stab_super_effective():
    assert attack(fire_poke, grass_poke, fire_move) == 258
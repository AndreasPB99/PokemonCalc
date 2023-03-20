from pokemon import Pokemon, Stats
from type import Type
from ability import *
from move import *

rattata_stats = Stats(hp=30, attack=56, defense=35, special_attack=25, special_defense=35, speed=72)
Rattata = Pokemon(id=19, type=(Type.NORMAL, None), stats=rattata_stats, moves=[Tackle], level=1, ability=Technician())
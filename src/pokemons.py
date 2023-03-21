from src.pokemon import Pokemon, Stats
from src.type import Type
from src.ability import *
from src.move import *

rattata_stats = Stats(hp=205, attack=205, defense=205, special_attack=205, special_defense=205, speed=205)
Rattata = Pokemon(id=19, type=(Type.NORMAL, None), stats=rattata_stats, moves=[Tackle], level=100, ability=Technician())
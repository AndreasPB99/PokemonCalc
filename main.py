from src.pokemons import Rattata
from src.move import *
from src.damage_calc import attack

if __name__ == '__main__':
    print(attack(Rattata, Rattata, Tackle))

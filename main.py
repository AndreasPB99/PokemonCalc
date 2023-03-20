from pokemons import Rattata
from move import *
from damage_calc import attack

if __name__ == '__main__':
    print(attack(Rattata, Rattata, Tackle))

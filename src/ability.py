from abc import ABC
from src.move import Move


class Ability(ABC):
    name = ''

    def attack(self, move):
        pass

    def defense(self, move):
        pass

    def status(self, move):
        pass

    def __str__(self):
        pass


class Nothing(Ability):
    name = 'nothing'


class Technician(Ability):
    name = 'technician'

    def attack(self, move: Move):
        if move.power < 60:
            move.power *= 1.5

    def __str__(self):
        return 'lower power moves are 50% more effective'

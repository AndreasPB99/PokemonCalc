from dataclasses import dataclass
from src.type import Type


@dataclass
class Move:
    type: Type
    power: int
    hits: int
    special: bool

    def on_hit(self):
        pass


Nothing = Move(type=Type.NORMAL, power=0, hits=0, special=False)
Tackle = Move(type=Type.NORMAL, power=40, hits=1, special=False)
Headbutt = Move(type=Type.NORMAL, power=60, hits=1, special=False)



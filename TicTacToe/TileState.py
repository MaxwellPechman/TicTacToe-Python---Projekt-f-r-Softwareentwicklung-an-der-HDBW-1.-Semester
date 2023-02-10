from enum import Enum

class TileState(Enum):
    EMPTY = ' '
    CROSS = 'X'
    CIRCLE = 'O'

    def getOpposite(self) -> 'TileState':
        if self == self.CIRCLE:
            return self.CROSS

        elif self == self.CROSS:
            return self.CIRCLE
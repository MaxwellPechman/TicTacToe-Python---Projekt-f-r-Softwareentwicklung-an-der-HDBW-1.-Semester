from TileState import TileState
from Tile import Tile

class Board:
    def __init__(self, size):
        self.tiles = list()
        self.size = size

        self.setupBoard()

    def setupBoard(self):
        row = 0

        while row < self.size:
            column = 0

            while column < self.size:
                self.tiles.append(Tile(row, column, TileState.EMPTY))

                column = column + 1
            row = row + 1

    def getSize(self) -> int:
        return self.size

    def setSize(self, size):
        self.size = size

    def getWinner(self):
        cond = list()
        state: TileState = TileState.EMPTY

        cond.append(self.checkRows())
        cond.append(self.checkColumns())
        cond.append(self.checkTopToBottom())
        cond.append(self.checkBottomToTop())

        for state in cond:
            if state != TileState.EMPTY:
                return state

        return state

    def checkRow(self, row) -> 'TileState':
        state = self.getTile(row, 0).getState()
        column = 0

        if state != TileState.EMPTY:
            while column < self.size:
                if state != self.getTile(row, column).getState():
                    return TileState.EMPTY

                column = column + 1

        return state

    def checkRows(self) -> 'TileState':
        row = 0

        while row < self.size:
            state = self.checkRow(row)

            if state != TileState.EMPTY:
                return state

            row = row + 1

        return TileState.EMPTY

    def checkColumn(self, column) -> 'TileState':
        state = self.getTile(column, 0).getState()
        row = 0

        if state != TileState.EMPTY:
            while row < self.size:
                if state != self.getTile(row, column).getState():
                    return TileState.EMPTY

                row = row + 1

        return state

    def checkColumns(self) -> 'TileState':
        column = 0

        while column < self.size:
            state = self.checkColumn(column)

            if state != TileState.EMPTY:
                return state

            column = column + 1

        return TileState.EMPTY

    # Checking diagonally from the top left corner to the lower right corner.
    def checkTopToBottom(self) -> 'TileState':
        state = self.getTile(0, 0).getState()

        if state != TileState.EMPTY:
            coord = 0

            while coord < self.size:
                if state != self.getTile(coord, coord).getState():
                    return TileState.EMPTY

                coord = coord + 1

        return state

    # Checking diagonally from the bottom left corner to the upper right corner.
    def checkBottomToTop(self) -> 'TileState':
        row = self.size - 1
        state = self.getTile(row, 0).getState()

        if state != TileState.EMPTY:
            column = 0

            while column < self.size:
                if state != self.getTile(row, column).getState():
                    return TileState.EMPTY

                column = column + 1
                row = row - 1

        return state

    def display(self):
        row = 0

        while row < self.size:
            column = 0
            line = "|"

            while column < self.size:
                line = line + str(self.getTile(row, column).getState().value) + "|"
                column = column + 1

            print(line)
            row = row + 1

    def getTile(self, row, column) -> 'Tile':
        tile: Tile
        for tile in self.tiles:
            if tile.getRow() == row and tile.getColumn() == column:
                return tile

    def getEmptyTiles(self):
        empty = list()
        tile: Tile

        for tile in self.tiles:
            if tile.getState() == TileState.EMPTY:
                empty.append(tile)

        return empty

    def isFull(self):
        tile: Tile
        for tile in self.tiles:
            if tile.getState() == TileState.EMPTY:
                return False

        return True
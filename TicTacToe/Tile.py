from TileState import TileState

class Tile:
    def __init__(self, row, column, state: TileState):
        self.row = row
        self.column = column
        self.state: TileState = state

    def getRow(self):
        return self.row

    def setRow(self, row):
        self.row = row

    def getColumn(self):
        return self.column

    def setColumn(self, column):
        self.column = column

    def getState(self) -> 'TileState':
        return self.state

    def setState(self, state: TileState):
        self.state = state
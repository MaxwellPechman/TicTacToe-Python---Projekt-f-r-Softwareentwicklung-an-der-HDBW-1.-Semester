import os
import random

from TileState import TileState
from Board import Board

clear = lambda: os.system('cls')

class TicTacToe:
    def __init__(self):
        self.isRunning = False
        self.board = None
        self.turn = 0
        self.player: TileState = self.getRandomPlayer()
        
        clear()
        self.updateGame()

    def getRandomPlayer(self) -> 'TileState':
        if random.randint(0, 1) == 0:
            return TileState.CROSS
        return TileState.CIRCLE

    def switchPlayer(self):
        if self.player == TileState.CROSS:
            self.player = TileState.CIRCLE

        elif self.player == TileState.CIRCLE:
            self.player = TileState.CROSS
    
    def __setupBoard(self):        
        try:
            size = int(input("[Game] Please enter the size of the field: "))
            
        except ValueError:
            print("[Error] Please define the size of the field with a number.")
            
            self.__setupBoard()
            
        else:
            if size > 0:
                self.board = Board(size)
                self.isRunning = True
                clear()
                pass

            else:
                print("[Error] field can not be smaller than one.")
                pass

    def updateGame(self):
        if self.isRunning:
            if not self.board.isFull():
                print("[Game] Round " + str(self.turn) + ". Player " + self.player.value + "'s turn.")
                self.board.display()

                try:
                    column: int = int(input("[Game] Player " + self.player.value + " has to choose a column: ")) - 1
            
                except ValueError:
                    print("[Error] Column needs to be a number.")
                    
                else:
                    if 0 <= column < self.board.getSize():
                        try:
                            row: int = int(input("[Game] Player " + self.player.value + " has to choose a row: ")) - 1
            
                        except ValueError:
                            print("[Error] Row needs to be a number.")
                            
                        else:
                            if 0 <= row < self.board.getSize():
                                if self.board.getTile(row, column).getState() == TileState.EMPTY:
                                    self.board.getTile(row, column).setState(self.player)

                                    winner: TileState = self.board.getWinner()
                                    if winner != TileState.EMPTY:
                                        clear()
                                        self.isRunning = False
                                        print("[Game] Game over! Player " + self.player.value + " has won the game!")
                                        self.board.display()
                                        return

                                    self.switchPlayer()
                                    self.turn = self.turn + 1
                                    clear()
                                    pass

                                else:
                                    print("[Error] This tile has already been selected by player " +
                                    self.board.getTile(row, column).getState().value + ".")
                                    pass

                            else:
                                print("[Error] Please select a row within the range of 1 and " + str(self.board.getSize()) + ".")
                                pass

                    else:
                        print("[Error] Please select a column within the range of 1 and " + str(self.board.getSize()) + ".")
                        pass

            else:
                print("[Game] Game over! The game ends in a tie.")
                self.board.display()
                return

        else:
            self.__setupBoard()

        self.updateGame()


# Run the game
def main():
    TicTacToe()


if __name__ == "__main__":
    main()
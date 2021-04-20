from Game import Game, GameError
from abc import ABC, abstractmethod


class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            #Type check
            try:
                row = int(input("Which row? "))
                col = int(input("Which column? "))
            except ValueError:
                print("Invalid Input; Expected 1,2 or 3")
                continue
            #range check
            if 1 <= row <= 3 and 1<= col <= 3:
                try:
                    self._game.play(row, col)
                except GameError:
                    print("Invalid Input")
            else:
                print("Row and column must be between 1 and 3")
        print(self._game)
        w = self._game.winner
        if w == Game.DRAW:
            print("The game was drawn")
        else:
            print(f"The winner was {w}")

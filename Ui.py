from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("running gui")

class Terminal(Ui):
    def __init__(self):
        self.__game = Game()

    def run(self):
        while not self.__game.winner:
            print(self.__game)
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
            self.__game.play(row, column)
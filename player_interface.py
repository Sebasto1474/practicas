from abc import ABC, abstractmethod
from random import choice

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    def make_move(self):
        new_move = choice(self.moves)
        x, y = self.position
        dx, dy = new_move
        self.position = ( x + dx, y + dy)
        self.path.append(self.position)
        return self.position
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1),(-1,0),(1,0)]
    def level_up(self):
        self.moves.extend([(1,1),(1,-1),(-1,1),(-1,-1)])

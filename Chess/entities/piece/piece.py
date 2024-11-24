from abc  import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, piecetype, color):
        self.piecetype = piecetype
        self.color = color
    
    @abstractmethod
    def valid_move(self, start_cell, end_cell):
        pass

class Cell:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def remove_piece(self):
        self.piece = None
    
    def put_piece(self, piece):
        self.piece = piece

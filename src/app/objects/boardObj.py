from .coordObj import Coord

class Board:
    def __init__(self, boardArr:list):
        self.board = boardArr
        self.sections = {}
        self.arr = []
        for row in boardArr:
            self.arr += row

    def GetCoord(self,coord:Coord):
        x = coord.x
        y = coord.y
        self.board[y][x].name = coord.name
        return self.board[y][x]

    def __str__(self) -> str:
        boardStr = ''

        for row in self.board[::-1]:
            boardStr += ''.join([str(tile.render) for tile in row]) + "\n"

        return boardStr

    def __repr__(self) -> str:
        return str(self)



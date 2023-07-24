WIDTH = 11
HEIGHT = 11

class Coord:
    def __init__(self,x:int,y:int, name:str = ''):
        self.x = x
        self.y = y
        self.name = name

    # Checks if coord exists in the board
    def Exists(self, width, height):
        cond1 = 0 <= self.x < width
        cond2 = 0 <= self.y < height
        return cond1 and cond2

    @property
    def Up(self) -> 'Coord':
        return Coord(self.x, self.y + 1,'up')

    @property
    def Down(self) -> 'Coord':
        return Coord(self.x, self.y - 1,'down')

    @property
    def Left(self) -> 'Coord':
        return Coord(self.x - 1, self.y,'left')

    @property
    def Right(self) -> 'Coord':
        return Coord(self.x + 1, self.y,'right')

    @property
    def Sides(self) -> list:
        sides = [
            self.Up,
            self.Down,
            self.Left,
            self.Right
        ]

        return [s for s in sides if s.Exists(11,11)]

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def __repr__(self) -> str:
        return str(self)

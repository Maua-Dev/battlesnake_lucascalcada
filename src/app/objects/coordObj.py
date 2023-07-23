class Coord:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

    def Up(self):
        if(self.y < 10): 
            return Coord(self.x, self.y + 1)

    def Down(self):
        if(self.y > 0):
            return Coord(self.x, self.y - 1)

    def Left(self):
        if(self.x > 0): 
            return Coord(self.x - 1, self.y)

    def Right(self):
        if(self.x < 10):
            return Coord(self.x + 1, self.y)

    def Sides(self) -> list:
        sides = [
            self.Up(),
            self.Down(),
            self.Left(),
            self.Right()
        ]

        return [s for s in sides if s != None]

    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    def __repr__(self) -> str:
        return str(self)

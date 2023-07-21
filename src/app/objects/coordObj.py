from math import sqrt

class Coord:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

    @staticmethod
    def Distance(coord1,coord2):
        deltaX = coord1.x - coord2.x
        deltaY = coord1.y - coord2.y
        return sqrt(deltaX ** 2 + deltaY ** 2)

    def Up(self): 
        return Coord(self.x, self.y + 1)
    def Down(self): 
        return Coord(self.x, self.y - 1)
    def Left(self): 
        return Coord(self.x - 1, self.y)
    def Right(self): 
        return Coord(self.x + 1, self.y)


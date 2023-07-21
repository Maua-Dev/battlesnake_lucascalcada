from .coordObj import Coord

class Food(Coord):
    def __init__(self,x:int,y:int,playerHeadCoord:Coord):
        super().__init__(x,y)
        self.distanceToPlayer = self.Distance(self,playerHeadCoord)
        # print(self)
        # self.reachanble = True

    def __str__(self):
        return f'Food obj at ({self.x},{self.y}), distance to player: {self.distanceToPlayer}'

    def __repr__(self):
        return str(self)

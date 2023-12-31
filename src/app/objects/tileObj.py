from .coordObj import Coord

class Tile(Coord):
    types = {
        0: 'Empty',
        1: 'Dangerous Tile',
        2: 'Snake Tile',
        3: 'Food'
    }

    # Used for console debugging
    icons = [
        "▫",
        "▧",
        "■",
        "●"
    ]

    def __init__(self,x:int,y:int,value:int):
        super().__init__(x,y)
        self.section = None
        self.value = value
        self.section = ''

    @property
    def render(self):
        return Tile.icons[self.value]

    @property
    def coord(self):
        return Coord(self.x,self.y)

    def __str__(self) -> str:
        return f'{Tile.types[self.value]} tile at ({self.x},{self.y})'

    def __repr__(self) -> str:
        return str(self)

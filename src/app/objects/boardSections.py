from .coordObj import Coord
from .boardParser import Board, Tile

#
#   Splits the board into sections to see if the player fits in an area
#

class SectionFinder():
    def __init__(self,board:Board):
        self.__board = board
        self.__boardTiles = board.arr
        self.__sections = {}
        
        # Create starting sections 
        for i,tile in enumerate(self.__boardTiles):
            tile.section = i
            self.sections[i] = [tile]

        self.FindSections()

    @property
    def board(self):
        return self.__board

    @property
    def sections(self):
        return self.__sections

    # Splits the board into sections
    def FindSections(self):
        for tile in self.__boardTiles:
            if(tile.value in (1,2)): 
                del self.sections[tile.section]
                tile.section = -1
                continue
            for sideTile in self.GetConnectedTiles(tile):
                if(sideTile.section > tile.section):
                    self.MergeSections(tile.section,sideTile.section)

    # Merges two sections into one
    def MergeSections(self,parent,child):
        for tile in self.sections[child]:
            tile.section = parent
        self.sections[parent] += self.sections[child]
        del self.sections[child]

    # Find adjancent tiles that are not walls or snakes
    def GetConnectedTiles(self,tile:Tile):
        tiles = [self.__board.GetCoord(t) for t in tile.Sides if self.__board.GetCoord(t).value not in [1,2]]
        return tiles

    # Prints tiles numbered by section to make debugging easier
    def __str__(self):
        objStr = ''

        for row in self.__board.board:
            sections = [tile.section for tile in row]
            keys = list(self.sections.keys())
            rowStr = ''
            for section in sections:
                if(section != -1):
                    rowStr += str(keys.index(section))
                else:
                    rowStr += '#'

            objStr += rowStr + '\n'

        return objStr
    
    def __repr__(self):
        return str(self)

from random import choice
from .coordObj import Coord
from .boardObj import Board
from .tileObj import Tile
from .boardSections import SectionFinder

class Parser:
    def __init__(self, boardData, playerSnake):
        self.__boardData = boardData
        self.__playerSnake = playerSnake

        # Player head coord
        self.__headPos = Coord(
            self.__playerSnake['head']['x'],
            self.__playerSnake['head']['y']
        )

        # Board without section data
        board = Board(self.GenBoardArr())
        self.__board = board
        
        # Populate board
        self.GetFood()
        self.GetSnakes()
        self.SnakeTails()
        self.DangerousTiles()

        # Splits board sections
        sectionFinder = SectionFinder(self.__board)

        # Update board data
        self.__board = sectionFinder.board
        self.__sections = sectionFinder.sections

        # Calculate area sizes
        self.SmallAreas()

    @property
    def board(self):
        return self.__board

    # Generates initial board array
    def GenBoardArr(self) -> list:
        board = [[Tile(x,y,0) for x in range(11)] for y in range(11)]
        return board

    # Find all food tiles
    def GetFood(self) -> None:
        for food in self.__boardData['food']:
            coord = Coord(food['x'],food['y'])
            self.__board.GetCoord(coord).value =  3


    # Find all snake tiles
    def GetSnakes(self) -> None:
        for snake in self.__boardData['snakes']:
            for tile in snake['body']:
                coord = Coord(tile['x'],tile['y'])
                self.__board.GetCoord(coord).value = 2


    # Sets next snake head coord as dangerous tiles
    def DangerousTiles(self) -> None:
        snakes = self.__boardData['snakes']
        for s in snakes:
            if s['id'] != self.__playerSnake['id']:
                head = s['head']
                headCoord = Tile(head['x'], head['y'], 1)
                for s in headCoord.Sides:
                    tile = self.__board.GetCoord(s)
                    # If a food is near an enemy snake's head, consider as inaccessible
                    # Chances are that the enemy will move into that tile
                    if tile.value == 3:
                        tile.value = 2
                    tile.value = 1

    # Remove Snake's tails
    def SnakeTails(self):
        for snake in self.__boardData['snakes']:
            if snake['length'] > 2:
                tail = snake['body'][-1]
                tailCoord = Coord(tail['x'],tail['y'])
                self.__board.GetCoord(tailCoord).value = 0

    # Sets areas that the snake cant fit as dangerous
    def SmallAreas(self) -> None:
        snakeLen = self.__playerSnake['length']
        for key in self.__sections:
            sectionSize = len(self.__sections[key])
            if(sectionSize < snakeLen):
                for tile in self.__sections[key]:
                    self.__board.GetCoord(tile).value = 1

    # Searches for the best tile to move to
    def FindSafeTiles(self) -> str:
        tiles = self.FindTiles()
        if(tiles == []): 
            tiles = self.FindLargestArea()
            return tiles[0]
        return choice(tiles)

    def FindTiles(self):
        dirs = []
        for direction in self.__headPos.Sides:
            val = self.__board.GetCoord(direction).value
            if(val == 0 or val == 3):
                dirs.append(direction.name)
        return dirs

    # Find tile with largest area
    def FindLargestArea(self):
        dirs = []
        for side in self.__headPos.Sides:
            tile = self.__board.GetCoord(side)
            if(tile.value == 1 and tile.section != -1):
                dirs.append(self.__board.GetCoord(side))
        
        # if the snake has no available options, go up
        if(dirs ==[]): return ['up']

        # sorts available tiles by area size
        dirs.sort(key= lambda t: len(self.__sections[t.section]), reverse=True)

        return [dir.name for dir in dirs]

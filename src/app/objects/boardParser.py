from random import choice
from .coordObj import Coord
from .boardObj import Board
from .tileObj import Tile
from .boardSections import SectionFinder

class Parser:
    def __init__(self, boardData, playerSnake):

        self.__boardData = boardData
        self.__playerSnake = playerSnake
        self.__headPos = Coord(
            self.__playerSnake['head']['x'],
            self.__playerSnake['head']['y']
        )
        #self.__foodArr = self.GetFood()
        self.__boardArr = self.GenBoardArr()

        # Board without section data
        board = Board(self.__boardArr)


        # Splits board sections
        sectionFinder = SectionFinder(board)

        # Update board data
        self.__board = sectionFinder.board
        self.__sections = sectionFinder.sections

        # Populate board
        self.GetFood()
        self.SmallAreas()

    @property
    def board(self):
        return self.__board

    # Find all snake tiles
    def GetSnakes(self) -> list:
        snakeTiles = []

        for snake in self.__boardData['snakes']:
            for tile in snake['body']:
                tile = Tile(tile['x'], tile['y'], 2)
                tile.danger += 999
                snakeTiles.append(tile)

        return snakeTiles

    # Sets next snake head coord as dangerous tiles
    def DangerousTiles(self) -> list:
        tiles = []
        snakes = self.__boardData['snakes']

        for s in snakes:
            if s['id'] != self.__playerSnake['id']:
                head = s['head']
                headCoord = Tile(head['x'], head['y'], 1)
                # Gerando erro aqui
                # Ta retornando tile fora do tabuleiro
                for s in headCoord.Sides:
                    tile = Tile(s.x,s.y,1)
                    tile.danger += 5
                    tiles.append(tile)
        return tiles

    # Sets areas that the snake cant fit as dangerous
    def SmallAreas(self):
        snakeLen = self.__playerSnake['length']
        for key in self.__sections:
            sectionSize = len(self.__sections[key])
            if(sectionSize < snakeLen):
                for tile in self.__sections[key]:
                    tile.value = 1
                    tile.danger = snakeLen - sectionSize
           # if(len(self.__sections[key]) < self.__playerSnake['length'] + 2):
           #     for tile in self.__sections[key]:
           #         print(f"Tile {tile} at {tile.coord} dangerous")
           #         self.__board.GetCoord(tile.coord).value = 1


    # Find all food tiles
    def GetFood(self) -> None:
        for food in self.__boardData['food']:
            coord = Coord(food['x'],food['y'])
            self.__board.GetCoord(coord).value =  3

    def GenBoardArr(self) -> list:
        # 0: safe tiles
        # 1: possibly dangerous
        # 2: bad  tiles 
        # 3: food tiles
        board = [[Tile(x,y,0) for x in range(11)] for y in range(11)]

        # Possibly dangerous tiles
        for tile in self.DangerousTiles():
            board[tile.y][tile.x] = tile

        # Tiles to avoid
        for snakeTile in self.GetSnakes():
            board[snakeTile.y][snakeTile.x] = snakeTile

        # Tiles considered safe
        #for tail in self.GetTails():
        #    board[tail.y][tail.x] = tail

        return board

    # TODO: there's a better way to do this
    # First check if 0 tiles exist
    # If not, choose a 1 tile if it exits
    # If not, there are no safe diretcions, move up
    
    # See if a float approach for a tile value is better
    def FindSafeTiles(self) -> str:
        tiles = self.FindTiles([0,3])
        #print(tiles)
        if(tiles == []): 
            #print('No 0 or 3 tiles found')
            tiles = self.FindLargestArea()
            #print('1 tiles : ',tiles)
            return tiles[0]
        return choice(tiles)

    def FindTiles(self, find):
        dirs = []
        for direction in self.__headPos.Sides:
            if(self.__board.GetCoord(direction).value in find):
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

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
        self.__foodArr = self.GetFood()
        self.__boardArr = self.GenBoardArr()

        # Board without section data
        board = Board(self.__boardArr)

        # Splits board sections
        sectionFinder = SectionFinder(board)

        # Update board data
        self.__board = sectionFinder.board
        self.__sections = sectionFinder.sections

    @property
    def board(self):
        return self.__board
    # Find all snake tiles
    def GetSnakes(self) -> list:
        snakeTiles = []

        for snake in self.__boardData['snakes']:
            for tile in snake['body']:
                tile = Tile(tile['x'], tile['y'], 2)
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
                tiles += [Tile(c.x,c.y,1) for c in headCoord.Sides()]
        return tiles

    # Sets snake's tails as safe tiles
    # removed because it's very inconsistent
    #def GetTails(self) -> list:
    #    tails = []
    #    snakes = self.__boardData['snakes']

    #    for s in snakes:
    #        tail = s['body'][-1]
    #        # Only enemy snakes' tails are safe
    #        if (s['id'] != self.playerId):
    #            tails.append(Tile(tail['x'], tail['y'], 0))


    #    return tails

    # Find all food tiles
    def GetFood(self) -> list:
        foodObjs= []

        for food in self.__boardData['food']:
            foodObjs.append(Tile(food['x'], food['y'], 3))

        return foodObjs

    def GenBoardArr(self) -> list:
        # 0: safe tiles
        # 1: possibly dangerous
        # 2: bad  tiles 
        # 3: food tiles
        board = [[Tile(x,y,0) for x in range(11)] for y in range(11)]

        # Fill food spots
        for food in self.__foodArr:
            board[food.y][food.x] = food

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
    def FindSafeTiles(self) -> list:
        dirs = []
        headX = self.__headPos.x
        headY = self.__headPos.y

            # check left
        if(headX > 0 and self.__boardArr[headY][headX - 1].value not in (1,2)):
            dirs.append('left')

        # check right
        if(headX < 10 and self.__boardArr[headY][headX + 1].value not in (1,2)):
            dirs.append('right')
            
        # check up
        if(headY < 10 and self.__boardArr[headY + 1][headX].value not in (1,2)):
            dirs.append('up')

        # check down
        if(headY > 0 and self.__boardArr[headY - 1][headX].value not in (1,2)):
            dirs.append('down')

        return dirs

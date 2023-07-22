from .coordObj import Coord

class Tile(Coord):
    types = {
        0: 'Empty',
        1: 'Wall',
        2: 'Food'
    }
    def __init__(self,x:int,y:int,value:int):
        super().__init__(x,y)
        self.section = None
        self.value = value
        self.section = ''

    def __str__(self) -> str:
        return f'{Tile.types[self.value]} tile at ({self.x},{self.y})'

    def __repr__(self) -> str:
        return str(self)

class Board:
    def __init__(self, boardArr:list):
        self.board = boardArr
        self.arr = []
        for row in boardArr:
            self.arr += row

    def GetCoord(self,coord:Coord):
        x = coord.x
        y = coord.y
        return self.board[y][x]

    def __str__(self) -> str:
        boardStr = ''

        for row in self.board[::-1]:
            boardStr += ''.join([str(tile) for tile in row]) + "\n"

        return boardStr

    def __repr__(self) -> str:
        return str(self)

class Parser:
    def __init__(self, boardData, playerSnake):
        head = playerSnake['head']

        self.__boardData = boardData
        self.playerId = playerSnake['id']
        self.headPos = Coord(head['x'],head['y'])

        self.foodArr = self.GetFood()
        self.boardArr = self.GenBoardArr()

        self.board = Board(self.boardArr)

    # Find all snake tiles
    def GetSnakes(self) -> list:
        snakeTiles = []

        for snake in self.__boardData['snakes']:
            for tile in snake['body']:
                tile = Tile(tile['x'], tile['y'], 1)
                snakeTiles.append(tile)

        return snakeTiles

    # Sets next snake head coord as dangerous tiles
    def DangerousTiles(self) -> list:
        tiles = []
        snakes = self.__boardData['snakes']

        for s in snakes:
            if s['id'] != self.playerId:
                head = s['head']
                headCoord = Tile(head['x'], head['y'], 1)
                tiles += headCoord.Sides()

        return tiles

    # Sets snake's tails as safe tiles
    def GetTails(self) -> list:
        tails = []
        snakes = self.__boardData['snakes']

        for s in snakes:
            tail = s['body'][-1]
            tails.append(Tile(tail['x'], tail['y'], 0))

        return tails

    # Find all food tiles
    def GetFood(self) -> list:
        foodObjs= []

        for food in self.__boardData['food']:
            foodObjs.append(Tile(food['x'], food['y'], 2))

        return foodObjs

    def GenBoardArr(self) -> list:
        # 0: safe tiles
        # 1: bad  tiles 
        # 2: food tiles
        board = [[Tile(x,y,0) for x in range(11)] for y in range(11)]

        # Fill food spots
        for food in self.foodArr:
            board[food.y][food.x] = food

        # Tiles to avoid
        for snakeTile in self.GetSnakes():
            board[snakeTile.y][snakeTile.x] = snakeTile

        # Tiles considered safe
        for tail in self.GetTails():
            board[tail.y][tail.x] = tail

        # Possibly dangerous tiles
        for tile in self.DangerousTiles():
            board[tile.y][tile.x] = tile

        return board

    # TODO: there's a better way to do this
    def FindSafeTiles(self) -> list:
        dirs = []
        headX = self.headPos.x
        headY = self.headPos.y

        # check left
        if(headX > 0 and self.boardArr[headY][headX - 1].value != 1):
            dirs.append('left')

        # check right
        if(headX < 10 and self.boardArr[headY][headX + 1].value != 1):
            dirs.append('right')
            
        # check up
        if(headY < 10 and self.boardArr[headY + 1][headX].value != 1):
            dirs.append('up')

        # check down
        if(headY > 0 and self.boardArr[headY - 1][headX].value != 1):
            dirs.append('down')

        return dirs

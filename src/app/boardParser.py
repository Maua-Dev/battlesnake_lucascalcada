from utils import Coord

class Board:
    def __init__(self, boardData, playerSnake):
        self.__boardData = boardData
        self.__playerSnake = playerSnake
        head = playerSnake["head"]
        self.headPos = Coord(head['x'],head['y'])
        self.food = self.GetFoodCoords()
        self.enemySnakesTiles = self.GetSnakes()
        self.boardObj = self.GenBoardArr()

    # Find all snake tiles
    def GetSnakes(self) -> list:
        tiles = []
        for snake in self.__boardData['snakes']:
            #if snake['id'] == self.__playerId: continue
            for tile in snake['body']:
                tile = Coord(tile['x'],tile['y'])
                tiles.append(tile)
        return tiles

    # Find all food tiles
    def GetFoodCoords(self) -> list:
        food = []
        for food in self.__boardData['food']:
            coord = Coord(food['x'], food['y'])
            food.append(coord)
        return food

    def GenBoardArr(self) -> list:
        # 0: safe tiles
        # 1: bad  tiles 
        # 2: food tiles
        board = [[0 for x in range(11)] for y in range(11)]

        # Fill food spots
        for food in self.food:
            board[food.y][food.x] = 2

        # Fill snake spots
        for snakeTile in self.enemySnakesTiles:
            board[snakeTile.y][snakeTile.x] = 1

        return board
    
    # TODO: there's a better way to do this
    def FindSafeTiles(self):
        headX = self.headPos.x
        headY = self.headPos.y
        dirs = []
        if(headX > 0):
            # check left
            if(self.boardObj[headY][headX - 1]): dirs.append('left')
        if(headX < 10):
            # check right
            if(self.boardObj[headY][headX + 1]): dirs.append('right')
        if(headY > 0):
            # check up
            if(self.boardObj[headY + 1][headX]): dirs.append('up')
            pass
        if(headY < 10):
            # check down
            if(self.boardObj[headY - 1][headX]): dirs.append('down')
        return dirs

    def __str__(self) -> str:
        boardStr = ''
        for row in self.boardObj:
            boardStr += ''.join(self.boardObj[row]) + "\n"
        return boardStr

    def __repr__(self):
        return str(self)

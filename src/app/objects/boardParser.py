from .coordObj import Coord
from .foodObj import Food

class Board:
    def __init__(self, boardData, playerSnake):
        self.__boardData = boardData
        head = playerSnake["head"]
        self.headPos = Coord(head['x'],head['y'])
        self.food = self.GetFood()
        self.enemySnakesTiles = self.GetSnakes()
        self.boardObj = self.GenBoardArr()
        print(self)

    # Find all snake tiles
    def GetSnakes(self) -> list:
        snakeTiles = []
        for snake in self.__boardData['snakes']:
            #if snake['id'] == self.__playerId: continue
            for tile in snake['body']:
                tile = Coord(tile['x'],tile['y'])
                snakeTiles.append(tile)
        return snakeTiles

    # Find all food tiles
    def GetFood(self) -> list:
        foodObjs= []
        for food in self.__boardData['food']:
            foodObjs.append(Food(food['x'], food['y'], self.headPos))
        # Sorts food tiles by distance to player head
        foodObjs = sorted(foodObjs, key=lambda x: x.distanceToPlayer)
        return foodObjs

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

    def GetNextHeadTile(self, coord: Coord):
        return self.boardObj[coord.y][coord.x]
    
    # TODO: there's a better way to do this
    def FindSafeTiles(self):
        headX = self.headPos.x
        headY = self.headPos.y
        dirs = []
        # check left
        if(headX > 0 and self.boardObj[headY][headX - 1] != 1):
            dirs.append('left')
        # check right
        if(headX < 10 and self.boardObj[headY][headX + 1] != 1):
            dirs.append('right')
        # check up
        if(headY < 10 and self.boardObj[headY + 1][headX] != 1):
            dirs.append('up')
        # check down
        if(headY > 0 and self.boardObj[headY - 1][headX] != 1):
            dirs.append('down')
        return dirs

    def __str__(self) -> str:
        boardStr = ''
        for row in self.boardObj[::-1]:
            boardStr += ''.join([str(tile) for tile in row]) + "\n"
        return boardStr

    def __repr__(self):
        return str(self)

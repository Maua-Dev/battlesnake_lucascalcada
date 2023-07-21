from fastapi import FastAPI
from mangum import Mangum
from random import choice
from parser import Board
from utils import Coord

app = FastAPI()

@app.get('/')
def read_root():
    # Snake customization
    return {
      'apiversion': '1',
      'author': 'LucasCalcada',
      'color': '#950aff',
      'head': 'caffeine',
      'tail': 'rbc-necktie',
      'version': '0.0.1-beta'
    }

@app.post('/start')
def start():
    pass

@app.post('/end')
def end():
    return

# Random movements tests
@app.post('/move')
def move(req: dict):
    playerSnake = req['you']
    headPos = Coord(
        playerSnake['head']['x'],
        playerSnake['head']['y']
    )
    board = Board(req['board'],playerSnake)
    dirs = board.FindSafeTiles()
    dir = choice(dirs)
    return {
        'move': dir,
        'shout': f'moving {dir}!'
    }

handler = Mangum(app, lifespan='off')

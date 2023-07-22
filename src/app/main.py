from fastapi import FastAPI
from mangum import Mangum
from random import choice
from .objects.boardParser import Parser
from .objects.coordObj import Coord

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
    boardParser = Parser(req['board'],playerSnake)

    dirs = boardParser.FindSafeTiles()
    dir = choice(dirs) if len(dirs) > 0 else 'up'

    return {
        'move': dir,
        'shout': f'moving {dir}!'
    }

handler = Mangum(app, lifespan='off')

from fastapi import FastAPI
from mangum import Mangum
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
    print('='* 30)
    print('NEW GAME STARTED')
    print('='* 30)

@app.post('/end')
def end():
    return

# Random movements tests
@app.post('/move')
def move(req: dict):
    playerSnake = req['you']
    boardParser = Parser(req['board'],playerSnake)

    dir = boardParser.FindSafeTiles()
    #dir = choice(dirs) if len(dirs) > 0 else 'up'

    print('='* 30)
    print('Turn: ' + str(req['turn']))
    print(playerSnake['name'])
    #print('Available directions: ' + ' '.join(dirs))
    print('Chosen direction: ', dir)
    print(boardParser.board)
    print('='* 30)
    return {
        'move': dir,
        'shout': f'moving {dir}!'
    }

handler = Mangum(app, lifespan='off')

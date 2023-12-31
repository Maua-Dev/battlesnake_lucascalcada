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
      'version': '1.0-final'
    }

@app.post('/start')
def start():
    print('=' * 30 + '\nNew Game Started\n' + '=' * 30)

@app.post('/end')
def end():
    return

# Random movements tests
@app.post('/move')
def move(req: dict):
    playerSnake = req['you']
    boardParser = Parser(req['board'],playerSnake)

    dir = boardParser.FindSafeTiles()

    print(f'Turn: {req["turn"]}\n{playerSnake["name"]}\nChosen direction: {dir}\n{boardParser.board}')
    print('='* 30)
    return {
        'move': dir,
        'shout': f'moving {dir}!'
    }

handler = Mangum(app, lifespan='off')

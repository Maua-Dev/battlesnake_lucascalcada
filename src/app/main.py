from fastapi import FastAPI
from mangum import Mangum
from random import choice

app = FastAPI()

@app.get("/")
def read_root():
    # Snake customization
    return {
      "apiversion": "1",
      "author": "LucasCalcada",
      "color": "#950aff",
      "head": "caffeine",
      "tail": "rbc-necktie",
      "version": "0.0.1-beta"
    }


# Random movements tests
MOVES = ['up', 'down', 'left', 'right']
@app.post("/move")
def move(req: dict):
    dir = choice(MOVES)
    return {
        "move": dir,
        "shout": f"moving {dir}!"
    }

handler = Mangum(app, lifespan="off")

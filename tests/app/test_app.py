from src.app.main import read_root, move
from src.app.objects.boardSections import SectionFinder

class Test_App:
    def test_read_root(self):
        resp = read_root()
        
        assert resp == {
            "apiversion": "1",
            "author": "LucasCalcada",
            "color": "#950aff",
            "head": "caffeine",
            "tail": "rbc-necktie",
            "version": "1.0-final"
        }

    def test_move(self):
      reqEx = {
      "game": {
        "id": "game-id",
        "ruleset": {
          "name": "standard",
          "version": "v1.1.15",
          "settings": {
            "foodSpawnChance": 15,
            "minimumFood": 1,
            "hazardDamagePerTurn": 14
          }
        },
        "map": "standard",
        "source": "league",
        "timeout": 500
      },
      "turn": 14,
      "board": {
        "height": 11,
        "width": 11,
        "food": [
          {"x": 5, "y": 5}, 
          {"x": 9, "y": 0}, 
          {"x": 2, "y": 6}
        ],
        "hazards": [
          {"x": 3, "y": 2}
        ],
        "snakes": [
          {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [
              {"x": 10, "y": 9}, 
              {"x": 10, "y": 10}, 
              {"x": 9, "y": 10}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "customizations":{
              "color":"#FF0000",
              "head":"pixel",
              "tail":"pixel"
            }
          }, 
          {
            "id": "snake-b67f4906-94ae-11ea-bb37",
            "name": "Another Snake",
            "health": 16,
            "body": [
              {"x": 9, "y": 8}, 
              {"x": 9, "y": 7}, 
              {"x": 9, "y": 6},
              {"x": 9, "y": 5}
            ],
            "latency": "222",
            "head": {"x": 9, "y": 8},
            "length": 4,
            "shout": "I'm not really sure...",
            "customizations":{
              "color":"#26CF04",
              "head":"silly",
              "tail":"curled"
            }
          }
        ]
      },
      "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 10, "y": 9}, 
          {"x": 10, "y": 10}, 
          {"x": 9, "y": 10}
        ],
        "latency": "111",
        "head": {"x": 10, "y": 9},
        "length": 3,
        "shout": "why are we shouting??",
        "customizations": {
          "color":"#FF0000",
          "head":"pixel",
          "tail":"pixel"
        }
      }
    }
      response = move(reqEx)
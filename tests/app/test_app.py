from src.app.main import read_root, move


class Test_App:
    def test_read_root(self):
        resp = read_root()
        
        assert resp == {
            "apiversion": "1",
            "author": "LucasCalcada",
            "color": "#950aff",
            "head": "caffeine",
            "tail": "rbc-necktie",
            "version": "0.0.1-beta"
        }

    def test_move(self):
        reqExample = {
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
                  {"x": 0, "y": 0}, 
                  {"x": 1, "y": 0}, 
                  {"x": 2, "y": 0}
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
                  {"x": 5, "y": 4}, 
                  {"x": 5, "y": 3}, 
                  {"x": 6, "y": 3},
                  {"x": 6, "y": 2}
                ],
                "latency": "222",
                "head": {"x": 5, "y": 4},
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
              {"x": 0, "y": 0}, 
              {"x": 1, "y": 0}, 
              {"x": 2, "y": 0}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "customizations": {
              "color":"#FF0000",
              "head":"pixel",
              "tail":"pixel"
            }
          }
        }
        response = move(reqExample)

    #def test_get_item(self):
    #    
    #    resp = read_item(1)

    #    assert resp == {"item_id": 1}

    #def test_post_item(self):
    #    request = {"item_id": 1,
    #               "name": "test"}

    #    resp = create_item(request)

    #    assert resp == {"item_id": 1,
    #                    "name": "test"}

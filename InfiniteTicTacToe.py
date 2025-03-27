#Empty board

empty_board = '1|2|3\n-----\n4|5|6\n-----\n7|8|9'

class Game:
    def __init__(self, occupied_boxes, board=empty_board):
        self.occupied_boxes = occupied_boxes
        self.board = board
        
    def change_board(self, )
        

class Board:    


class Player:
    def __init__(self, game, shape, box=0):
        self.game = game
        self.shape = shape
        self.box = box
        
    def choose_box(self):
        while self.box <= 0 or self.box >= 10 and self.box not in self.game.occupied_boxes:
            self.box = input()
        

game = Game([])
print(game.board)
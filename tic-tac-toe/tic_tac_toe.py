import re
import random
import numbers

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    if (self.board[0] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL) or (self.board[2] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL):
      self.is_game_over = True
      self.winner = _PLAYER
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL) or (self.board[2] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL):
      self.is_game_over = True
      self.winner = _MACHINE
    elif (self.board[0] == _PLAYER_SYMBOL and self.board[1] == _PLAYER_SYMBOL and self.board[2] == _PLAYER_SYMBOL) or (self.board[3] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL) or (self.board[6] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL):
      self.is_game_over = True
      self.winner = _PLAYER
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[1] == _MACHINE_SYMBOL and self.board[2] == _MACHINE_SYMBOL) or (self.board[3] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL) or (self.board[6] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL):
      self.is_game_over = True
      self.winner = _MACHINE
    elif (self.board[0] == _PLAYER_SYMBOL and self.board[3] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL) or (self.board[1] == _PLAYER_SYMBOL and self.board[4] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL) or (self.board[2] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL):
      self.is_game_over = True
      self.winner = _PLAYER
    elif (self.board[0] == _MACHINE_SYMBOL and self.board[3] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL) or (self.board[1] == _MACHINE_SYMBOL and self.board[4] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL) or (self.board[2] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL):
      self.is_game_over = True
      self.winner = _MACHINE 
    else:
      self.is_game_over = False
    result = self.is_game_over
    return result
    
  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.is_over()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.is_over()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    for cell in self.ran_number():
      if self.board[cell] is None or self.board[cell] != _PLAYER_SYMBOL:
        self.board[cell] = _MACHINE_SYMBOL
        break
        
        
  
  def ran_number(self):
    for cel in range(0, len(self.board)-1):
      var = map(int, random.randint(0, len(self.board)-1).as_integer_ratio())
      return var
     

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    if self.turn == _PLAYER:
      print("The winner is " + self.winner)
    elif self.turn == _MACHINE:
      print("The winner is " + self.winner)

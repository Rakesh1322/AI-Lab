class TicTacToe:

  def __init__(self):
    self.values = ["-", "-", "-", 
                  "-", "-", "-", 
                  "-", "-", "-"]
    self.player = "x"


  def show_board(self):
    print(f"{self.values[0]} | {self.values[1]} | {self.values[2]}")
    print(f"{self.values[3]} | {self.values[4]} | {self.values[5]}")
    print(f"{self.values[6]} | {self.values[7]} | {self.values[8]}")


  def play_game(self):
    self.show_board()
    for i in range(9):
      self.handle_turn(self.values)
      if self.check_tie() or self.winner():
        break


  def handle_turn(self, values):
    try:
      turn = int(input(f"Player {self.player} pick a square (1-9) from left to right: "))
    except ValueError:
      self.handle_turn(self.values)
      return
    
   
    if self.values[turn-1] == "x" or self.values[turn-1] == "o":
      print("That square has been played already!")
      self.handle_turn(self.values)
    else:
      self.values[turn-1] = self.player
      self.show_board()
    self.flip_player()


  def winner(self):
    self.row_winner = self.check_rows()
    self.column_winner = self.check_columns()
    self.diagonal_winner = self.check_diagonals()
    if self.row_winner:
      winner = self.check_rows()
      print(f"{winner} has won the game!")
      return True
    elif self.column_winner:
      winner = self.check_columns()
      print(f"{winner} has won the game!")
      return True
    elif self.diagonal_winner:
      winner = self.check_diagonals()
      print(f"{winner} has won the game!")
      return True


  def check_rows(self):
    row1 = self.values[0] == self.values[1] == self.values[2] != "-"
    row2 = self.values[3] == self.values[4] == self.values[5] != "-"
    row3 = self.values[6] == self.values[7] == self.values[8] != "-"
    if row1:
      return self.values[0]
    elif row2:
      return self.values[3]
    elif row3:
      return self.values[6]  
  

  def check_columns(self):
    col1 = self.values[0] == self.values[3] == self.values[6] != "-"
    col2 = self.values[1] == self.values[4] == self.values[7] != "-"
    col3 = self.values[2] == self.values[5] == self.values[8] != "-"
    if col1:
      return self.values[0]
    elif col2:
      return self.values[1]
    elif col3:
      return self.values[2]


  def check_diagonals(self):
    dia1 = self.values[0] == self.values[4] == self.values[8] != "-"
    dia2 = self.values[2] == self.values[4] == self.values[6] != "-"
    if dia1:
      return self.values[0]
    elif dia2:
      return self.values[2]


  def check_tie(self):
    if "-" not in self.values:
      print("Game is a tie!")
      return True
    else:
      return False


  def flip_player(self):
    if self.player == "x":
      self.player = "o"
    else:
      self.player = "x"

if __name__ == "__main__":
  new_board = TicTacToe()
  new_board.play_game()
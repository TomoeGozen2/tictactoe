


import random 

class TicTacToe(): 
  
  def __init__(self): 
    self.board = []
    self.player = None
    self.continue_game = True
    self.computer_piece = None
  
  def create_board(self): 
    for i in range(3):
      row = []
      for j in range(3):
        row.append('-')
      self.board.append(row)
      
    
#user input for selecting spot on board

    
  def select_spot(self):
    global computer_piece
    try:
        computer_row = random.randint(0,2)
        computer_column = random.randint(0,2)

        row = int(input('Enter your preferred row: '))
        column = int(input('Enter your preferred column: '))

        if row >= 0 and row <= 2 and self.board[row][column] == '-' and self.board[row][column] != computer_piece:
            self.board[row][column] = player
        if column >= 0 and column <= 2 and self.board[row][column] == '-' and self.board[row][column] != computer_piece:
            self.board[row][column] = player
        if self.board[computer_row][computer_column] != self.board[row][column]:
            self.board[computer_row][computer_column] = computer_piece
        #Winning condition
    
        #Top row
        elif self.board[0][0] and self.board[0][1] and self.board[0][2] == player:
           print('You win')
           self.continue_game = False
        #Left side
        elif self.board[0][0] and self.board[1][0] and self.board[2][0] == player:
           print('You win')
           self.continue_game = False
        #Right side
        elif self.board[0][2] and self.board[1][2] and self.board[2][2] == player:
           print('You win')
           self.continue_game = False
        #Left to right diagonal
        elif self.board[0][0] and self.board[1][1] and self.board[2][2] == player:
           print('You win')
           self.continue_game = False
        #Right to left diagonal
        elif self.board[0][2] and self.board[1][1] and self.board[2][0] == player:
           print('You win')
           self.continue_game = False
        #Middle column
        elif self.board[0][1] and self.board[1][1] and self.board[2][1] == player:
           print('You win')
           self.continue_game = False
        #bottom row
        elif self.board[2][0] and self.board[2][1] and self.board[2][2] == player:
          print('You win')
          self.continue_game = False
        #middle row
        elif self.board[1][0] and self.board[1][1] and self.board[1][2] == player:
          print('You win')
          self.continue_game = False
      
        
        
        
        else:
            print('That place is already taken. Try again. ')
        
    except:
        print('Out of scope. Try again. ')
    
    return self.board
  
  def print_board(self):
  

      print(self.board[0])
      print(self.board[1])
      print(self.board[2])
    
  def game_loop(self):
    global player
    global computer_piece
    
    user_select = input('Do you want X\'s or O\'s?').upper()
    if user_select == 'X':
        player = user_select
        computer_piece = 'O'
    elif user_select == 'O':
        player = user_select
        computer_piece = 'X'
    while self.continue_game:
      self.print_board()
      self.select_spot()
      
      

tic_tac_toe = TicTacToe()
tic_tac_toe.create_board()
tic_tac_toe.game_loop()
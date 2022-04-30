import sys
import random
import time

play_list = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

positions = [
    [0,0], [0,1], [0,2],
    [1,0], [1,1], [1,2],
    [2,0], [2,1], [2,2],
]    

game_ended = False
play_count = 0
is_player_turn = True
player_mark = ""
computer_mark = ""

def print_board():
   print(" ------------------------------- ")
   print("|          |          |         |")
   print(f"|    {play_list[0][0]}     |    {play_list[0][1]}     |    {play_list[0][2]}    |")
   print("|          |          |         |")
   print(" ------------------------------- ")
   print("|          |          |         |")
   print(f"|    {play_list[1][0]}     |    {play_list[1][1]}     |    {play_list[1][2]}    |")
   print("|          |          |         |")
   print(" ------------------------------- ")
   print("|          |          |         |")
   print(f"|    {play_list[2][0]}     |    {play_list[2][1]}     |    {play_list[2][2]}    |")
   print("|          |          |         |")
   print(" ------------------------------- ")

def play():
    global is_player_turn
    global player_mark
    global computer_mark
    player_mark = choose_mark()
    computer_mark = "X"
    if(player_mark == "X"): computer_mark = "O"

    print(f"You play {player_mark} while computer plays {computer_mark}")

    while not game_ended:
        if is_player_turn: set_mark(player_mark)
        # replace auto_play with set_mark here
        # to enable a dual player game (without computer)
        else: auto_play(computer_mark)   
        is_player_turn = not is_player_turn 

#Logic for computer's moves
def auto_play(computer_mark: str):
    global play_count
    position = random.choice(positions)
    x = position[0]
    y = position[1]
    positions.remove(position)
    play_count += 1
    play_list[x][y] = computer_mark
    print("\nComputer's turn\n")
    time.sleep(0.5)
    print_board()
    evaluate(x, y, computer_mark)

def set_mark(mark: str):
    global play_count
    global positions
    print("\nYour turn")
    can_play = True
    while can_play:
        coordinates = input("Enter coordinates [e.g 0,0]: ").split(",")
        if len(coordinates) != 2: print("Invalid coordinates")
        else:
            try:
                x = int(coordinates[0])
                y = int(coordinates[1])
                if is_position_available(x,y):
                    positions.remove([x,y])
                    play_count += 1
                    play_list[x][y] = mark
                    print("\n")
                    print_board()
                    can_play = evaluate(x, y, mark)
                else: continue
            except Exception as err:
                 #print(f"{err}")
                 print("Invalid coordinates")
                 continue

def evaluate(x: int, y: int, mark: str) -> bool:
    #diagonals
    if not evaluate_right_diagonal(x,y,mark):
        return prompt_play_again()
    if not evaluate_left_diagonal(x,y,mark):
        return prompt_play_again()
    #columns
    if not evaluate_column(y,mark):
        return prompt_play_again()
    #rows
    if not evaluate_row(x,mark):
        return prompt_play_again()

    #check for draw
    if play_count==9:
       print("It's a draw")
       return prompt_play_again()

    return False

def evaluate_column(y: int, mark: str) -> bool:
     #go through the column
    if play_list[0][y] == mark and play_list[1][y] == mark and play_list[2][y] == mark:
        declare_winner(mark)
        return False
    return True

def evaluate_row(x: int,mark: str) -> bool:
     #go across the row
    if play_list[x][0] == mark and play_list[x][1] == mark and play_list[x][2] == mark:
        declare_winner(mark)
        return False
    return True

def evaluate_right_diagonal(x: int, y: int, mark: str) -> bool:
    if (x==0 and y==0) or (x==1 and y==1) or (x==2 and y==2):
        if play_list[0][0] == mark and play_list[1][1] == mark and play_list[2][2] == mark:
              declare_winner(mark)
              return False
    return True

def evaluate_left_diagonal(x: int, y: int, mark: str) -> bool:
    if (x==0 and y==2) or (x==1 and y==1) or (x==2 and y==0):
        if play_list[0][2] == mark and play_list[1][1] == mark and play_list[2][0] == mark:
              declare_winner(mark)
              return False
    return True

def prompt_play_again() -> bool:
    global is_player_turn
    global game_ended
    global play_count
    global play_list
    global positions
    choice = ""
    while choice not in ["Y", "N"]:
       choice = input("Do you want to play again? (Y/N): ").upper()
    
    if choice == "Y":
        #reset global state
        is_player_turn = True
        game_ended = False
        play_count = 0
        positions = [
    [0,0], [0,1], [0,2],
    [1,0], [1,1], [1,2],
    [2,0], [2,1], [2,2],
]
        play_list = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
        play()
        return False
    else:
        sys.exit()

def is_position_available(x: int, y: int) -> bool:
    if x>2 or x<0 or y>2 or y<0: 
        print("Coordinate is not available")
        return False
    if play_list[x][y].strip()=="":
        return True
    print("Coordinate is not available")
    return False

def choose_mark() -> str:
    mark = ""
    while mark not in ["X" , "O"]:
        mark = input("Choose your mark (X or O): ").strip().upper()
    return mark

def declare_winner(mark: str):
    if mark == player_mark: print("You win")
    else: print("Computer wins")

if __name__ == "__main__":
    play()
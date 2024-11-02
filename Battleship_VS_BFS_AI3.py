#Player's Turn
#This part contains code for the player’s move input and marking hits/misses on the AI’s board.
def player_move(board):
    #Geting player's shot coordinates and validate input.
    while True:
        try:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter col (0-9): "))
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if board[row][col] == "~" or board[row][col] == "S":
                    return row, col
                else:
                    print("You already shot there. Try again.")
            else:
                print("Out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def check_hit(board, row, col):
    #Check if the shot is a hit or miss.
    if board[row][col] == "S":
        board[row][col] = "X"  # Mark as hit
        return True
    board[row][col] = "O"  # Mark as miss
    return False

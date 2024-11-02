#Placing Ships on the Board
#This part contains functions to place ships randomly on the boards.
def place_ship(board, ship_size):
    #Randomly placing a ship of a given size on the board.
    while True:
        orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - ship_size)
            if all(board[row][col + i] == "~" for i in range(ship_size)):
                for i in range(ship_size):
                    board[row][col + i] = "S"
                break
        else:
            row = random.randint(0, BOARD_SIZE - ship_size)
            col = random.randint(0, BOARD_SIZE - 1)
            if all(board[row + i][col] == "~" for i in range(ship_size)):
                for i in range(ship_size):
                    board[row + i][col] = "S"
                break

def setup_game():
    #Seting up the game boards for both player and AI by placing ships.
    player_board = create_board()
    ai_board = create_board()
    
    for ship_size in SHIP_SIZES:
        place_ship(player_board, ship_size)
        place_ship(ai_board, ship_size)
    
    return player_board, ai_board

#Game Setup and Utility Functions
#This part includes the initial setup for the game board and ships.
import random
from collections import deque

BOARD_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2]  # Represent sizes of each ship

def create_board():
    #Creating an empty game board.
    return [["~"] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def print_board(board, hide_ships=False):
    #Printing the board to the console, optionally hiding ships.
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            if cell == "S" and hide_ships:
                row_display.append("~")
            else:
                row_display.append(cell)
        print(f"{i} " + " ".join(row_display))
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
#AI’s Move Using BFS
#This part implements the AI’s BFS logic for targeting cells after a hit.
def bfs_ai_move(player_board, hit_queue, visited):
    #AI move with BFS: expands search around hit cells.
    if not hit_queue:
        # If no current target, choose a random cell
        while True:
            row, col = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
            if (row, col) not in visited:
                visited.add((row, col))
                return row, col
    else:
        # BFS targeting: expand search around hit cells in the queue
        row, col = hit_queue.popleft()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d_row, d_col in directions:
            new_row, new_col = row + d_row, col + d_col
            if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                return new_row, new_col
    return None, None
#Battleship_VS_BFS_AI2
#This part contains the main game loop, where both players take turns, and a victory check function.
def play_round(player_board, ai_board, hit_queue, visited):
    #Playing one round: both player and AI take a turn.
    print("\nYour Board:")
    print_board(player_board)
    print("\nAI's Board (hidden):")
    print_board(ai_board, hide_ships=True)
    
    print("\nYour Turn:")
    row, col = player_move(ai_board)
    if check_hit(ai_board, row, col):
        print("Hit!")
    else:
        print("Miss!")
    
    print("\nAI's Turn:")
    row, col = bfs_ai_move(player_board, hit_queue, visited)
    if row is not None and col is not None:
        print(f"AI fires at ({row}, {col})")
        if check_hit(player_board, row, col):
            print("AI hit your ship!")
            hit_queue.append((row, col))  # Add to queue if it's a hit
        else:
            print("AI missed.")

def check_victory(board):
    #Checking if all ships on a board have been sunk.
    return all(cell != "S" for row in board for cell in row)

def main():
    player_board, ai_board = setup_game()
    hit_queue = deque()  # Queue for BFS targeting when a ship is hit
    visited = set()  # Track visited cells to avoid re-guessing
    
    print("Welcome to Battleship with BFS AI!")
    while True:
        play_round(player_board, ai_board, hit_queue, visited)
        
        if check_victory(ai_board):
            print("\nCongratulations! You sunk all of the AI's ships!")
            break
        elif check_victory(player_board):
            print("\nGame over! The AI sunk all of your ships.")
            break

# Start the game
main()

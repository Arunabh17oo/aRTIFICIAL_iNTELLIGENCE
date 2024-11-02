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

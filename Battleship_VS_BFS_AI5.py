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

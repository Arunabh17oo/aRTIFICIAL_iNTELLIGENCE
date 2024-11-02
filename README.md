Part 1: Game Setup and Utility Functions
This part includes the initial setup for the game board and ships.
     Explanation:
Constants: BOARD_SIZE and SHIP_SIZES define the game’s board size (10x10) and the sizes of ships to place on the board.
create_board(): Initializes an empty 10x10 grid for both players and AI, where "~" indicates an empty cell.
print_board(): Outputs the board to the console. Ships can be hidden (for the AI board) or displayed (for the player’s board).
Part 2: Placing Ships on the Board
This part contains functions to place ships randomly on the boards.
     Explanation:
place_ship(): Randomly places a ship of the given size on the board, either horizontally or vertically. Ships are only placed in locations where they don’t overlap with others.
setup_game(): Creates two boards (one for the player and one for the AI) and places all ships on both boards.
Part 3: Player's Turn
This part contains code for the player’s move input and marking hits/misses on the AI’s board.
    Explanation:
player_move(): Prompts the player to enter the coordinates of their shot, ensuring valid input within the board’s bounds. It only accepts cells that haven't been targeted yet.
check_hit(): Checks if the player’s shot hits ("X") or misses ("O") on the board.
Part 4: AI’s Move Using BFS
This part implements the AI’s BFS logic for targeting cells after a hit.
    Explanation:
bfs_ai_move(): Controls the AI's targeting logic.
If hit_queue is empty, it chooses a random cell.
If a hit has occurred, it performs BFS by checking adjacent cells (up, down, left, right) to sink the ship.
Coordinates are stored in visited to avoid repeating moves, and successful hits are added to hit_queue to continue BFS in subsequent turns.
Part 5: Gameplay Loop and Victory Check
This part contains the main game loop, where both players take turns, and a victory check function.
    Explanation:
play_round(): Manages each game round where the player and AI each take a turn.
Displays both boards, handles player moves, and AI moves with BFS targeting.
check_victory(): Checks if all ships on a board have been sunk.
main(): The main function initializes the game setup, creates the hit_queue and visited set for AI, and runs the gameplay loop until there is a winner.
This structure provides a clean, step-by-step understanding of each component in the game!

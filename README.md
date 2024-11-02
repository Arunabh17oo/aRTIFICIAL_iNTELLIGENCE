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





To run this Battleship with BFS AI game, you’ll need Python installed on your system. Here’s a step-by-step guide:

Steps to Run the Game
*Install Python (if not already installed):

*Download and install Python from python.org.
*During installation, make sure to check the option to add Python to your PATH.
*Save the Code:

*Open a text editor (like VS Code, Sublime Text, or Notepad).
*Copy the entire code provided and paste it into the editor.
*Save the file with a .py extension, e.g., battleship_game.py.
*Open a Terminal:

*Navigate to the directory where you saved battleship_game.py.
*On Windows, you can use Command Prompt or PowerShell.
*On macOS/Linux, you can use the Terminal app.
*Run the Game:

*In the terminal, type the following command and press Enter:
bash
python battleship_game.py
This command will start the game in the terminal.
*Play the Game:

Follow the on-screen prompts:
Player’s Turn: You’ll be asked to enter a row and column number (from 0 to 9) to guess the location of the AI's ships.
AI’s Turn: The AI will fire at random initially, and once it hits, it will use BFS to target adjacent cells.
Game End:

The game ends when either you or the AI sink all of the opponent's ships.
You’ll receive a victory or game-over message based on the outcome.
Example of Terminal Interaction
Player's Turn: Enter a row and column when prompted.


Enter row (0-9): 3
Enter col (0-9): 5
AI's Turn: The AI automatically takes its shot and shows the result.
That’s it! You can now play and enjoy the Battleship game with BFS AI right from your terminal.

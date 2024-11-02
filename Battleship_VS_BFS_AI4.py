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

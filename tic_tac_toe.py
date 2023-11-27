import random

# Step 3: Board Representation
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_board():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Step 4: Player Input
def get_player_move(player):
    while True:
        try:
            if player == 'X':
                row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
                col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            else:
                row, col = get_computer_move()
                
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Step 5: Game Logic
def check_win(player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Step 6: Display
def play_game():
    player_turn = 'X'

    while True:
        print_board()
        row, col = get_player_move(player_turn)
        board[row][col] = player_turn

        if check_win(player_turn):
            print_board()
            print(f"Player {player_turn} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break

        player_turn = 'O' if player_turn == 'X' else 'X'

# Step 7: Computer Move
def get_computer_move():
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

# Step 8: Loop and Play
if __name__ == "__main__":
    play_game()
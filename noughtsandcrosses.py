import random
import os.path
import json

random.seed()

def draw_board(board):
    """
    Function to print the current state of the game board.

    Parameters:
    - board (list of lists): The game board.
    """
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def welcome(board):
    """
    Welcome message and initial display of the game board.

    Parameters:
    - board (list of lists): The game board.
    """
    print("Welcome to Noughts and Crosses!")
    draw_board(board)

def initialise_board(board):
    """
    Initialize the game board with empty spaces.

    Parameters:
    - board (list of lists): The game board.

    Returns:
    - board (list of lists): The initialized game board.
    """
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Get and validate player move input.

    Parameters:
    - board (list of lists): The game board.

    Returns:
    - tuple: Player's chosen row and column.
    """
    while True:
        move = input("Enter your move (1-9): ")
        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3
        if board[row][col] == ' ':
            return row, col

def choose_computer_move(board):
    """
    Computer's move strategy.

    Parameters:
    - board (list of lists): The game board.

    Returns:
    - tuple: Computer's chosen row and column.
    """
    for i in range(1, 10):
        row, col = (i - 1) // 3, (i - 1) % 3
        if board[row][col] == ' ':
            board[row][col] = 'O'
            if check_for_win(board, 'O'):
                return row, col
            board[row][col] = ' '

    # If the player can win on the next move, block that
    for i in range(1, 10):
        row, col = (i - 1) // 3, (i - 1) % 3
        if board[row][col] == ' ':
            board[row][col] = 'X'
            if check_for_win(board, 'X'):
                board[row][col] = 'O'
                return row, col
            board[row][col] = ' '

    # Take the center if it's available
    if board[1][1] == ' ':
        return 1, 1

    # Take a corner if it's available
    for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[row][col] == ' ':
            return row, col

    # Take any other cell
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col

def check_for_win(board, mark):
    """
    Check if a player (X or O) has won.

    Parameters:
    - board (list of lists): The game board.
    - mark (str): The player's mark ('X' or 'O').

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    # Check horizontal spaces
    for row in board:
        if row.count(mark) == 3:
            return True

    # Check vertical spaces
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark or \
       board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False

def check_for_draw(board):
    """
    Check if the game is a draw.

    Parameters:
    - board (list of lists): The game board.

    Returns:
    - bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game(board):
    """
    Main game loop.

    Parameters:
    - board (list of lists): The game board.

    Returns:
    - int: 1 if player wins, -1 if computer wins, 0 if it's a draw.
    """
    board = initialise_board(board)
    draw_board(board)
    while True:
        # Player move
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Player X wins!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        # Computer move
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    """
    Display menu and get user choice.

    Returns:
    - str: User's choice.
    """
    print("1 - Play the game")
    print("2 - Save score in file 'leaderboard_2406794.txt'")
    print("3 - Load and display the scores from the 'leaderboard_2406794.txt'")
    print("q - End the program")
    return input("Enter your choice: ")

def load_scores():
    """
    Load scores from the leaderboard file.

    Returns:
    - dict: Leaderboard with player names and scores.
    """
    if os.path.exists('leaderboard_2406794.txt'):
        with open('leaderboard_2406794.txt', 'r') as f:
            try:
                leaders = json.load(f)
            except json.decoder.JSONDecodeError:
                leaders = {}
    else:
        leaders = {}
    return leaders

def save_score(score):
    """
    Save player's score to the leaderboard file.

    Parameters:
    - score (int): Player's score.
    """
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard_2406794.txt', 'w') as f:
        json.dump(leaders, f)

def display_leaderboard(leaders):
    """
    Display the leaderboard.

    Parameters:
    - leaders (dict): Leaderboard with player names and scores.
    """
    for name, score in leaders.items():
        print(f"{name}: {score}")

# Main program
# The flow of the program is driven by the play_game_2417489 function and menu choices

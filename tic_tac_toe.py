"""
Tic Tac Toe Game
----------------

This program simulates a classic two-player Tic Tac Toe game 
played on a 3x3 grid.
Players take turns marking a square with their respective symbols 
('X' or 'O').
The first player to get three of their symbols in a row 
— either horizontally, vertically, or diagonally — 
wins the game. 
If all squares are filled without a winner, the game ends in a tie.

Features:
- Displays the current board state after each move
- Validates player input to ensure a square isn't already taken
- Detects win conditions for rows, columns, and diagonals
- Detects tie conditions when the board is full and no winner exists
- Simple console interface for user interaction

Usage:
Run the script and follow the on-screen prompts to play.
Each player is asked to choose a square 
by entering a number corresponding to an open position.

This game is designed for educational purposes, 
demonstrating key programming concepts such as:
- Control flow
- User input validation
- Data structures (lists)
- Game logic and state management
"""
import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

GAMES_TO_WIN = 5

CONTINUE = {'y', 'yes', 'ok', 'sure', 'continue', 'go'}
DONT_CONTINUE = {'n', 'no', 'stop', 'quit', 'exit', 'end'}
VALID_CHOICES = CONTINUE | DONT_CONTINUE

WINNING_LINES = [
    (1, 2, 3),  # Top row
    (4, 5, 6),  # Middle row
    (7, 8, 9),  # Bottom row
    (1, 4, 7),  # Left column
    (2, 5, 8),  # Middle column
    (3, 6, 9),  # Right column
    (1, 5, 9),  # Diagonal from top left to bottom right
    (3, 5, 7)   # Diagonal from top right to bottom left
]

PLAYER_TURNS = {'player', 'p'}
COMPUTER_TURNS = {'computer', 'c'}
VALID_TURNS = list(PLAYER_TURNS | COMPUTER_TURNS)

def show_numbered_board():
    """
    Display a numbered board for Tic Tac Toe
    to help players understand the square positions.
    """
    print('''
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
    ''')
def join_or(strings, delim=', ', final_delim='or'):
    """
    Join a list of strings
    and use a final delimiter for the last value.

    PARAM: strings - list of strings to join
    PARAM: delim - string to use between values (default is ', ')
    PARAM: final_delim - string to use before the last value

    returns: a string with the strings joined appropriately
    """
    if len(strings) == 0:
        return ''

    if len(strings) == 1:
        return str(strings[0])

    if len(strings) == 2:
        return f"{strings[0]} {final_delim} {strings[1]}"

    end = strings[-1]
    first = strings[:-1]

    return f"{delim.join(map(str, first))}{delim}{final_delim} {end}"

def display_board(board, p_score=None, c_score=None):
    """
    Display the current Tic Tac Toe board and optionally the score.
    
    PARAM: board - the game board
    PARAM: p_score - current player score (optional)
    PARAM: c_score - current computer score (optional)
    """
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')

    if p_score is not None and c_score is not None:
        print('')
        print(f"Player: {p_score} | Enemy: {c_score}")

def initialize_board():
    """
    Initial function to initialize an empty board dictionary 
    with empty spaces as strings
    """
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    """
    Return the prompt with an arrow pointing to it
    ===> message
    """
    print(f'===> {message}')
def player_chooses_square(board):
    """
    Prompt the player to choose an available square
    Fill that square with player choice X
    Checks for invalid input (string, number not in squares)

    PARAM: board - game board that displays on screen
    """
    valid_choices = [str(num) for num in empty_squares(board)]
    while True:
        prompt(f'Choose a square ({', '.join(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            board[int(square)] = HUMAN_MARKER
            break
        prompt(f"Invalid choice. Please choose from {join_or(valid_choices)}.")

def computer_chooses_square(board):
    """
    Computer chooses a square using simple AI:
    1. Try to win
    2. Block the player from winning
    3. Take the center if available
    4. Take a random corner
        *on second thought this made computer too difficult
    5. Take a random available square

    PARAM: board - game board dictionary representing the game state
    """
    def find_at_risk_square(marker):
        for line in WINNING_LINES:
            values = [board[sq] for sq in line]
            if values.count(marker) == 2 and values.count(INITIAL_MARKER) == 1:
                return line[values.index(INITIAL_MARKER)]
        return None

    # 1. Try to win
    square = find_at_risk_square(COMPUTER_MARKER)
    if square:
        board[square] = COMPUTER_MARKER
        return

    # 2. Block the player
    square = find_at_risk_square(HUMAN_MARKER)
    if square:
        board[square] = COMPUTER_MARKER
        return

    # 3. Take the center
    if board[5] == INITIAL_MARKER:
        board[5] = COMPUTER_MARKER
        return

    # # 4. Take a random corner
    # corners = [sq for sq in [1, 3, 7, 9] if board[sq] == INITIAL_MARKER]
    # if corners:
    #     board[random.choice(corners)] = COMPUTER_MARKER
    #     return

    # 5. Take any remaining square
    board[random.choice(empty_squares(board))] = COMPUTER_MARKER

def empty_squares(board):
    """
    Return a list of empty squares on the board
    Used to check if the board is full or not

    PARAM: board - game board that displays on screen

    RETURNS: list of available empty squares
    """
    return [square for square, value in board.items()
            if value == INITIAL_MARKER]

def board_full(board):
    """ 
    Check if the board is full

    PARAM: board - current state of the game board

    RETURNS: True if the board is full, False otherwise
    """
    return not empty_squares(board)

def someone_won(board):
    """ Check if someone has won the game

    PARAM: board - current state of the game board

    RETURNS: True if someone has won, False otherwise
    """
    return bool(detect_winner(board))

def detect_winner(board):
    """
    Check if there is a winner on the board

    PARAM: board - current state of the game board

    RETURNS: 'Player' if the player has won, 
             'Computer' if the computer has won, 
             None if there is no winner
    """
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER
        ): return 'Player'

        if (board[sq1] == COMPUTER_MARKER
              and board[sq2] == COMPUTER_MARKER
              and board[sq3] == COMPUTER_MARKER
        ): return 'Computer'
    return None

def play_again(message='Play again? (y or n)'):
    """
    Ask the player if they want to play again
    Validates the user input

    PARAM: message - message to display when asking to play again

    RETURNS: True if player wants to continue, False otherwise
    """
    prompt(message)
    answer = input().strip().lower()
    if answer in CONTINUE:
        return True
    if answer in DONT_CONTINUE:
        return False
    return play_again('That was not a valid choice. Please enter y or n:')

def score_and_result(board, p_score, c_score):
    winner = detect_winner(board)
    display_board(board)
    if winner:
        prompt(f'{winner} WON!')
        if winner == 'Player':
            p_score += 1
        else:
            c_score += 1
    else:
        prompt("It's a tie!")
    return p_score, c_score

def first_turn():
    """
    Ask player to choose who goes first
    If not choice is made, randomly select who goes first

    Returns 'player' or 'computer'
    """
    prompt("Who goes first? (player('p') or computer('c') or random)")
    answer = input().strip().lower()
    if answer in PLAYER_TURNS:
        return 'player'
    if answer in COMPUTER_TURNS:
        return 'computer'
    prompt("That was not a valid choice. Randomly selecting who goes first.")
    return random.choice(VALID_TURNS)

def choose_square(board, player, p_score, c_score):
    if player == 'player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)
    display_board(board, p_score, c_score)


def alternate_player(current_player):
    """
    Alternate the current player between 'player' and 'computer'

    PARAM: current_player - 'player' or 'computer'

    RETURNS: 'computer' if current_player is 'player', 
             'player' if current_player is 'computer'
    """
    return 'computer' if current_player == 'player' else 'player'

def play_tic_tac_toe():
    prompt("Welcome to Tic Tac Toe!")
    prompt("You are 'X'. Computer is 'O'.\n")

    prompt("You can choose a square by entering a number from 1 to 9.")
    prompt("The squares are numbered as follows:")
    show_numbered_board()
    prompt(f"First to {GAMES_TO_WIN} wins the match!\n")
    p_score = c_score = 0

    while True:
        board = initialize_board()
        prompt("New game started! Let's play Tic Tac Toe!\n")

        current_player = first_turn()
        display_board(board, p_score, c_score)

        while not (someone_won(board) or board_full(board)):
            choose_square(board, current_player, p_score, c_score)
            if someone_won(board) or board_full(board):
                break
            current_player = alternate_player(current_player)

        p_score, c_score = score_and_result(board, p_score, c_score)
        prompt(f"Score — Player: {p_score} | Enemy: {c_score}\n")


        if GAMES_TO_WIN in (p_score, c_score):
            prompt("CONGRATS! You WON the match!"
                   if p_score == GAMES_TO_WIN
                   else "Wow, you lost at tic tac toe. How sad."
                   )
            p_score = c_score = 0

        if not play_again():
            break

    prompt("Thanks for playing Tic Tac Toe!")

play_tic_tac_toe()
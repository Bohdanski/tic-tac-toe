import random
from IPython.display import clear_output

def display_board(board):
    '''
    Takes in a list and creates a board using ASCII art.
    Board spaces are assigned to list indexes.
    clear_output() function clears the previous board versions from the output.
    '''
    clear_output()
    print("╔═══╦═══╦═══╗")
    print (f"║ {board[7]} ║" + f" {board[8]} " + f"║ {board[9]} ║")
    print("╠═══╬═══╬═══╣")
    print (f"║ {board[4]} ║" + f" {board[5]} " + f"║ {board[6]} ║")
    print("╠═══╬═══╬═══╣")
    print (f"║ {board[1]} ║" + f" {board[2]} " + f"║ {board[3]} ║")
    print("╚═══╩═══╩═══╝")

def player_input():
    '''
    Starts with an empty string variable, and will continually ask the player to choose between
    and X or O marker. Function accepts both lower and upper case letters, and whatever mark is chosen first gets
    assigned to player 1, the other mark is assigned to player 2. Function returns player1 and player 2 marks in
    the form of a tuple, so that it may be unpacked later.
    '''
    marker = ''

    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player 1: Choose X or O: ')

    player1 = marker

    if player1.upper() == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1.upper(), player2.upper())

def place_marker(board, marker, position):
    '''
    Take in a board, marker value, and a position.
    Using the board, pass in the value given to the position parameter, as the value of the of board index.
    Set that equal to the value of the marker.
    '''
    board[position] = marker

def win_check(board, mark):
    '''
    Checks to see if one mark is on the board three times across either columns, rows, or diagonals.
    Must be set equal to mark otherwise if there are three consecutive blank spaces, the function will
    consider this as a win. Pass in a board value and player mark value, returns a boolean value.
    '''
    # Rows
    return ((board[1]==board[2]==board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or
    # Columns
    (board[1]==board[4]==board[7]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    # Diagonals
    (board[1]==board[5]==board[9]==mark) or
    (board[7]==board[5]==board[3]==mark))

def choose_first():
    '''
    Will randomly choose between a 1 or a 2, the function then returns this value to decide which player will go first.
    '''
    first = random.randint(1,2)
    print(f"Player {first} will go first")
    return first

def space_check(board, position):
    '''
    Pass in the board, and a parameter for position.
    Then check to see if an index on the board that is passed in, with a value equal to the position parameter
    is equal to blank. Retrun true or false.
    '''
    return board[position] == ' '

def full_board_check(board):
    '''
    Pass in a board. For every space on the board, check if each index between 1 through 9 is equal to blank.
    If it is return false, meaning that at least one of the boards indexes represents a blank space.
    Otherwise return true.
    '''
    for space in board:
        if (board[1] == ' ' or
            board[2] == ' ' or
            board[3] == ' ' or
            board[4] == ' ' or
            board[5] == ' ' or
            board[6] == ' ' or
            board[7] == ' ' or
            board[8] == ' ' or
            board[9] == ' '):
            return False
        else:
            return True

def player_choice(board, player):
    '''
    Pass in board and player parameters. Create a blank intiger called position.
    While position is not a value between 1 and 9, keep asking the player to pick an intiger value.
    Then check the space_check function using the same board, and the newly assigned position value
    to see if the space is open or not. If it is, return the value for that position,
    Otherwise promt the player to pick a new position.
    '''
    position = int()

    while not 1 <= position < 10:
        position = int(input(f"{player} pick your position on the board: "))

    if space_check(board, position) == True:
        return int(position)
    else:
        return f"Position {position} on the board is currently filled, please choose an empty position."

def replay():
    '''
    Create an empty string, ask the player if they want to play again by inputting y or n and assign that
    value to the the empty string. Keep asking until the right input is given, regardless of case.
    If value is y, return true, otherwise return false.
    '''
    replay_input = ''

    while replay_input.upper() != 'Y' and replay_input.upper() != 'N':
        replay_input = input("Would you like to play again (Y/N)? ")

    if replay_input.upper() == 'Y':
        return True
    else:
        return False

def player1_turn(player1):
    '''
    Pass in the player parameter, this should be the value from the unpacked tuple returned from the player_input function.
    Create a variable for position. Position is equal to value returned from the player_position function, after passing
    in the board currently being played on, and the mark being used for this player.
    If position is equal to an instance of an intiger. Then place the marker on the board at that position, check to see if
    the player has won and assign that to a variable, display what board should currently look like, and then return the
    the value for the variable checking if the player has won or not.
    Otherwise the function assumes the position the player has chosen is not available.
    '''
    position = player_choice(game_board, player1)

    if isinstance(position, int):
        place_marker(game_board, player1, position)

        check = win_check(game_board, player1)

        display_board(game_board)

        return check
    else:
        print(position)

def player2_turn(player2):
    '''
    Pass in the player parameter, this should be the value from the unpacked tuple returned from the player_input function.
    Create a variable for position. Position is equal to value returned from the player_position function, after passing
    in the board currently being played on, and the mark being used for this player.
    If position is equal to an instance of an intiger. Then place the marker on the board at that position, check to see if
    the player has won and assign that to a variable, display what board should currently look like, and then return the
    the value for the variable checking if the player has won or not.
    Otherwise the function assumes the position the player has chosen is not available.
    '''
    position = player_choice(game_board, player2)

    if isinstance(position, int):
        place_marker(game_board, player2, position)

        check = win_check(game_board, player2)

        display_board(game_board)

        return check
    else:
        print(position)


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')

    while True:
        # Set the game up here

        # Create a new board
        game_board = [" "]*10

        # Assign a value for who goes first
        choose = choose_first()

        # Unpack the tuple from player_input() and assign the values
        player1, player2 = player_input()

        # Turn the game state on to True
        game_on = True

        # While the game state is on:
        while game_on == True:
            # If player 1 is chosen first:
            if choose == 1:
                # Player 1 Turn:
                # Display the board.
                display_board(game_board)

                # Check to see if player 1 has won and the break out of the loop.
                if player1_turn(player1) == True:
                    print('Player 1 wins!')
                    break
                # Or check to see if there is a tie and break out of the board.
                elif full_board_check(game_board) == True:
                    print("It's a tie!")
                    break

                # Player 2 Turn:
                # Check to see if player 2 has won and the break out of the loop.
                if player2_turn(player2) == True:
                    print('Player 2 wins!')
                    break
                # Or check to see if there is a tie and break out of the board.
                elif full_board_check(game_board) == True:
                    print("It's a tie!")
                    break

                # Otherwise continue to iterate through this loop until a player wins
                # or until there is a tie.

            # If player 2 is chosen first:
            elif choose == 2:
                # Player 2 Turn:
                # Display the board.
                display_board(game_board)

                # Check to see if player 2 has won and the break out of the loop.
                if player2_turn(player2) == True:
                    print('Player 2 wins!')
                    break
                # Or check to see if there is a tie and break out of the board.
                elif full_board_check(game_board) == True:
                    print("It's a tie!")
                    break

                # Player 1 Turn:
                # Check to see if player 1 has won and the break out of the loop.
                if player1_turn(player1) == True:
                    print('Player 1 wins!')
                    break
                # Or check to see if there is a tie and break out of the board.
                elif full_board_check(game_board) == True:
                    print("It's a tie!")
                    break

        # If game_on loop is broken out of, execute this function, if the value is true then the outermost while loop
        # remains true and the process is looped again, otherwise the loop is broken out of.
        if not replay():
            break

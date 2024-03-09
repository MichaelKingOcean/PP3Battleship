

import random

# Function to create an empty board
def create_board(size):
    board = []
    for _ in range(size):
        row = ['O'] * size
        board.append(row)
    return board

# Function to print the board
def print_board(board):
    rowNumber = 1
    for row in board:
        print(" ".join(row))
        rowNumber += 1

# Function to place ships randomly on the board
def shipsLocation(board, num_ships):
    size = len(board)
    for _ in range(num_ships):
        ship_row = random.randint(0, size - 1)
        ship_col = random.randint(0, size - 1)
        board[ship_row][ship_col] = 'X'

# Function to check if the guess hits a ship
def check_guess(board, guess_row, guess_col):
    if board[guess_row][guess_col] == 'X':
        print("HIT!")
        board[guess_row][guess_col] = '!'
    else:
        print("MISS!")

# Main function to play the game
def play_battleship(board_size, num_ships, num_turns):
    board = create_board(board_size)
    shipsLocation(board, num_ships)
    
    print("Let's play Battleship!")
    for turn in range(num_turns):
        print(f"Turn {turn+1}")
        print_board(board)
        guess_row = int(input("Guess Row: \n")) -1
        guess_col = int(input("Guess Col: \n")) -1
        
        
        if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
            print("Invaild Entry")
        else:
            check_guess(board, guess_row, guess_col)
        
        if all(all(cell != 'X' for cell in row) for row in board):
            print("You've sunk all the battleships!")
            break
    else:
        print("Game Over. You've run out of turns.")

# Example usage:
play_battleship(7, 5, 15)  # Play with a 7x7 board, 5 ships, and 15 turns
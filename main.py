# Winning possibilities for Tic Tac Toe
winning_combos = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Array containing the choices of each player.
player1 = []
player2 = []

game_is_over = False


# Print the text-based game.
def print_tictactoe():
    print(f"- - - - - - -")
    print(f"| {grid[0]} | {grid[1]} | {grid[2]} |")
    print(f"- - - - - - -")
    print(f"| {grid[3]} | {grid[4]} | {grid[5]} |")
    print(f"- - - - - - -")
    print(f"| {grid[6]} | {grid[7]} | {grid[8]} |")
    print(f"- - - - - - -")


# Checks if any of the players met the winning condition.
def check_winner():
    if player1 in winning_combos:
        print("Player 1 Won!")
        game_is_over = True
        return exit()
    elif player2 in winning_combos:
        print("Player 2 Won!")
        game_is_over = True
        return exit()

print_tictactoe()
while game_is_over == False:    
    pick1 = int(input("Pick a number to place the X: "))
    while pick1 in player1 or pick1 in player2:
        pick1 = int(input(("This square has already been picked. Choose another one:\n")))
    player1.append(pick1)
    grid[pick1-1] = "X"
    print_tictactoe()
    check_winner()  
    pick2 = int(input("Pick a number to place the O: "))
    while pick2 in player1 or pick2 in player2:
        pick2 = int(input(("This square has already been picked. Choose another one:\n")))
    player2.append(pick2)
    grid[pick2-1] = "O"
    print_tictactoe()
    check_winner() 
    
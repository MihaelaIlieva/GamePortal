from tkinter import *
from tkinter import messagebox
import profilepage
import database.basicqueries as basicqueries
import datetime

username = ""
password = ""

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == '.':
                return False
    return True

def has_winner(board):

    for row in board:
        if row[0] != '.' and row[0] == row[1] and row[0] == row[2]:
            return True
        
    for col in range(3):
        if board[0][col] != '.' and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            return True
        
    if board[0][0] != '.' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    
    if board[0][2] != '.' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
    return False

def evaluate_state(board):
    for row in board:
        if row[0] == row[1] == row[2] == player_symbol:
            return -10
        elif row[0] == row[1] == row[2] == computer_symbol:
            return 10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player_symbol:
            return -10
        elif board[0][col] == board[1][col] == board[2][col] == computer_symbol:
            return 10

    if board[0][0] == board[1][1] == board[2][2] == player_symbol:
        return -10
    elif board[0][0] == board[1][1] == board[2][2] == computer_symbol:
        return 10
    if board[0][2] == board[1][1] == board[2][0] == player_symbol:
        return -10
    elif board[0][2] == board[1][1] == board[2][0] == computer_symbol:
        return 10
    return 0

def minimax(board, depth, is_maximizer, alpha, beta):
    score = evaluate_state(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_board_full(board):
        return 0
    if is_maximizer:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = computer_symbol
                    best = max(best, minimax(board, depth + 1, not is_maximizer, alpha, beta))
                    board[i][j] = '.'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = player_symbol
                    best = min(best, minimax(board, depth + 1, not is_maximizer, alpha, beta))
                    board[i][j] = '.'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = computer_symbol
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = '.'
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def save_progress(state):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    basicqueries.add_played_game(username, "tic_tac_toe", current_date, 0, state)

def try_again():
    global board, player_turn, game_over, new_root
    if new_root:
        new_root.destroy()
    board = [['.' for _ in range(3)] for _ in range(3)]
    player_turn = True
    game_over = False

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=NORMAL)

def back_to_profile():
    root.destroy()
    profilepage.ProfilePage(username, password)

def game_over_function():
    global new_root

    new_root = Toplevel()
    new_root.geometry('375x125+600+350')
    new_root.title("Game over")
    new_root.config(bg=MAIN_COLOUR)
    new_root.overrideredirect(True)

    try_again_button = Button(new_root, text="Нова игра", font=(None,16,'bold'), fg='white', bd=0, bg=MAIN_COLOUR, activebackground=MAIN_COLOUR, activeforeground='white', cursor='hand1', command=try_again)
    try_again_button.pack()
    back_to_profile_button = Button(new_root, text="Към профила ми", font=(None,16,'bold'), fg='white', bd=0, bg=MAIN_COLOUR, activebackground=MAIN_COLOUR, activeforeground='white', cursor='hand1', command=back_to_profile)
    back_to_profile_button.pack()

def on_click(row, col):
    global player_turn, game_over
    if not game_over and player_turn and board[row][col] == '.':
        buttons[row][col].config(text=player_symbol, state=DISABLED)
        board[row][col] = player_symbol
        player_turn = False
        if has_winner(board):
            messagebox.showinfo("Game Over", "You win!")
            game_over_function()
            save_progress("win")
            game_over = True
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            game_over_function()
            save_progress("draw")
            game_over = True
        else:
            row, col = find_best_move(board)
            buttons[row][col].config(text=computer_symbol, state=DISABLED)
            board[row][col] = computer_symbol
            if has_winner(board):
                messagebox.showinfo("Game Over", "Computer wins!")
                game_over_function()
                save_progress("loss")
                game_over = True
            elif is_board_full(board):
                messagebox.showinfo("Game Over", "It's a draw!")
                game_over_function()
                save_progress("draw")
                game_over = True
            player_turn = True

MAIN_COLOUR = '#160559'
root = Tk()
root.title("Tic Tac Toe")
root.geometry('1520x980')
root.config(bg=MAIN_COLOUR)


player_symbol = 'X'
computer_symbol = 'O'
player_turn = True
game_over = False

board = [['.' for _ in range(3)] for _ in range(3)]

buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = Button(root, text="", font=(None, 30), width=25, height=6,
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(button)
    buttons.append(row_buttons)

root.mainloop()
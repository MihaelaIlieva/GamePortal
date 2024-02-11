import datetime
import profilepage
import database.basicqueries as basicqueries
from tkinter import Tk, Button, messagebox, DISABLED, NORMAL, Toplevel

class TicTacToeGame:

    def __init__(self, username):
        self.username = username
        self.MAIN_COLOUR = '#160559'
        self.root = Tk()
        self.root.title("Tic Tac Toe")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg=self.MAIN_COLOUR)

        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        self.player_turn = True
        self.game_over = False

        self.board = [['.' for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = Button(self.root, text="", font=(None, 30), width=25, height=6,
                                command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.root.mainloop()

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '.':
                    return False
        return True

    def has_winner(self):

        for row in self.board:
            if row[0] != '.' and row[0] == row[1] and row[0] == row[2]:
                return True
            
        for col in range(3):
            if self.board[0][col] != '.' and self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col]:
                return True
            
        if self.board[0][0] != '.' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return True
        
        if self.board[0][2] != '.' and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return True
        return False

    def evaluate_state(self):
        for row in self.board:
            if row[0] == row[1] == row[2] == self.player_symbol:
                return -10
            elif row[0] == row[1] == row[2] == self.computer_symbol:
                return 10

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.player_symbol:
                return -10
            elif self.board[0][col] == self.board[1][col] == self.board[2][col] == self.computer_symbol:
                return 10

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player_symbol:
            return -10
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.computer_symbol:
            return 10
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player_symbol:
            return -10
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.computer_symbol:
            return 10
        return 0

    def minimax(self, depth, is_maximizer, alpha, beta):
        score = self.evaluate_state()
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if self.is_board_full():
            return 0
        if is_maximizer:
            best = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '.':
                        self.board[i][j] = self.computer_symbol
                        best = max(best, self.minimax(depth + 1, not is_maximizer, alpha, beta))
                        self.board[i][j] = '.'
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            break
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '.':
                        self.board[i][j] = self.player_symbol
                        best = min(best, self.minimax(depth + 1, not is_maximizer, alpha, beta))
                        self.board[i][j] = '.'
                        beta = min(beta, best)
                        if beta <= alpha:
                            break
            return best

    def find_best_move(self):
        best_val = float('-inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    self.board[i][j] = self.computer_symbol
                    move_val = self.minimax(0, False, float('-inf'), float('inf'))
                    self.board[i][j] = '.'
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

    def save_progress(self, state):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        basicqueries.add_played_game(self.username, "tic_tac_toe", current_date, 0, state)

    def try_again(self):
        if self.new_root:
            self.new_root.destroy()
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.player_turn = True
        self.game_over = False

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state=NORMAL)

    def back_to_profile(self):
        self.root.destroy()
        profilepage.ProfilePage(self.username)

    def game_over_function(self):
        self.new_root = Toplevel()
        self.new_root.geometry('375x125+600+350')
        self.new_root.title("Game over")
        self.new_root.config(bg=self.MAIN_COLOUR)
        self.new_root.overrideredirect(True)

        self.try_again_button = Button(self.new_root, text="Нова игра", font=(None,16,'bold'), fg='white', bd=0, bg=self.MAIN_COLOUR, activebackground=self.MAIN_COLOUR, activeforeground='white', cursor='hand1', command=self.try_again)
        self.try_again_button.pack()
        self.back_to_profile_button = Button(self.new_root, text="Към профила ми", font=(None,16,'bold'), fg='white', bd=0, bg=self.MAIN_COLOUR, activebackground=self.MAIN_COLOUR, activeforeground='white', cursor='hand1', command=self.back_to_profile)
        self.back_to_profile_button.pack()

    def on_click(self, row, col):
        if not self.game_over and self.player_turn and self.board[row][col] == '.':
            self.buttons[row][col].config(text=self.player_symbol, state=DISABLED)
            self.board[row][col] = self.player_symbol
            self.player_turn = False
            if self.has_winner():
                messagebox.showinfo("Game Over", "You win!")
                self.game_over_function()
                self.save_progress("win")
                self.game_over = True
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over_function()
                self.save_progress("draw")
                self.game_over = True
            else:
                row, col = self.find_best_move()
                self.buttons[row][col].config(text=self.computer_symbol, state=DISABLED)
                self.board[row][col] = self.computer_symbol
                if self.has_winner():
                    messagebox.showinfo("Game Over", "Computer wins!")
                    self.game_over_function()
                    self.save_progress("loss")
                    self.game_over = True
                elif self.is_board_full():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.game_over_function()
                    self.save_progress("draw")
                    self.game_over = True
                self.player_turn = True

if __name__ == '__main__':
    TicTacToeGame("mihaela")
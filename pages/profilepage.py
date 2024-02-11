import getrich
import mainpage
import tictactoepage
import statisticspage
from tkinter import Tk, Label, Button, PhotoImage

class ProfilePage:
    
    def __init__(self, username):
        self.username = username

        self.root = Tk()
        self.root.title("Game Portal - Profile Page")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.MAIN_COLOUR = '#100235'
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'

        self.background_label = Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_image = PhotoImage(file="images/pagebackground.png")
        self.background_label.configure(image=self.background_image)

        self.username_label = Label(self.root, text=f"Welcome {self.username}! What will it be today?", font=(None, 20), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.username_label.place(relx=0.5, rely=0.15, anchor="center")

        self.picture_label = Label(self.root, bg=self.MAIN_COLOUR)
        self.picture_label.place(relx=0.5, rely=0.35, anchor="center")
        self.picture_image = PhotoImage(file="images/background_old.png")
        self.picture_label.configure(image=self.picture_image)

        self.get_rich_button = Button(self.root, text="Get Rich", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_get_rich_page, width=15, height=2)
        self.get_rich_button.place(relx=0.5, rely=0.45, anchor="center")
        self.get_rich_button.place(relx=0.25, rely=0.6, anchor="center")

        self.tic_tac_toe_button = Button(self.root, text="Tic Tac Toe", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_tic_tac_toe_page, width=15, height=2)
        self.tic_tac_toe_button.place(relx=0.5, rely=0.55, anchor="center")
        self.tic_tac_toe_button.place(relx=0.40, rely=0.6, anchor="center")

        self.statistics_button = Button(self.root, text="Statistics", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_statistics_page, width=15, height=2)
        self.statistics_button.place(relx=0.5, rely=0.65, anchor="center")
        self.statistics_button.place(relx=0.55, rely=0.6, anchor="center")

        self.logout_button = Button(self.root, text="Logout", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.open_main_page, width=15, height=2)
        self.logout_button.place(relx=0.5, rely=0.75, anchor="center")
        self.logout_button.place(relx=0.70, rely=0.6, anchor="center")

        self.root.mainloop()

    def open_get_rich_page(self):
        self.root.destroy()
        getrich.GetRichGame(self.username)

    def open_tic_tac_toe_page(self):
        self.root.destroy()
        tictactoepage.TicTacToeGame(self.username)

    def open_statistics_page(self):
        self.root.destroy()
        statisticspage.StatisticsDisplay(self.username)

    def open_main_page(self):
        self.root.destroy()
        mainpage.MainPage()
        

if __name__ == "__main__":
    profile_page = ProfilePage("Username")

import profilepage
from database import basicqueries
from tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, Canvas, Scrollbar

class StatisticsDisplay:

    def __init__(self, username):
        self.root = Tk()
        self.username = username
        self.root.title("Statistics")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.config(bg='#160559')

        self.title_font = (None, 16, "bold")
        self.stats_font = (None, 12)
        self.highlight_color = '#ffb300'

        self.sort_options = ["Max Questions Answered", "First on", "TTT Wins", "TTT Draws", "TTT Losses"]
        self.sort_var = StringVar()
        self.sort_var.set(self.sort_options[0])

        self.profile_page_button = Button(self.root, text="Profile page", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.back_to_profile, width=15, height=2)
        self.profile_page_button.place(relx=0.95, rely=0.03, anchor="center")

        self.create_widgets()
        self.display_statistics()

        self.root.mainloop()

    def create_widgets(self):
        sort_label = Label(self.root, text="Sort By:", bg='#160559', fg='white', font=self.title_font)
        sort_label.pack(side="top", padx=10, pady=10)

        sort_menu = OptionMenu(self.root, self.sort_var, *self.sort_options)
        sort_menu.config(bg='#160559', fg='white', font=self.stats_font)
        sort_menu.pack(side="top", padx=10, pady=5)

        sort_button = Button(self.root, text="Sort", command=self.sort_statistics)
        sort_button.pack(side="top", padx=10, pady=5)

        self.canvas = Canvas(self.root, bg='#160559')
        scrollbar_x = Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        scrollbar_y = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)

        self.main_frame = Frame(self.canvas, bg='#160559')
        self.main_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")

        self.canvas.pack(side="left", fill="both", expand=True)

    def display_statistics(self):
        all_users_stats = {}
        all_users = basicqueries.get_all_users()
        for user in all_users:
            user_stats = {
                "MaxQuestionsAnswered": basicqueries.get_high_score_questions(user[1]),
                "First on": basicqueries.get_date_of_high_score_questions(user[1], basicqueries.get_high_score_questions(user[1])),
                "TTTWins": basicqueries.get_outcomes(user[1],"win"),
                "TTTDraws": basicqueries.get_outcomes(user[1],"draw"),
                "TTTLosses": basicqueries.get_outcomes(user[1],"loss")
            }
            all_users_stats[user[1]] = user_stats

        for i, (user, stats) in enumerate(all_users_stats.items()):
            bg_color = self.highlight_color if user == self.username else '#160559'

            user_label = Label(self.main_frame, text=user, font=self.title_font, bg=bg_color, fg='white', width=30, anchor="w")
            user_label.grid(row=i, column=0, sticky="ew")

            for j, (stat_name, stat_value) in enumerate(stats.items()):
                stat_label = Label(self.main_frame, text=f"{stat_name}: {stat_value}", font=self.stats_font, bg=bg_color, fg='white', width=30, anchor="w", wraplength=275)
                stat_label.grid(row=i, column=j+1, sticky="ew")

    def sort_statistics(self):
        sort_criteria = self.sort_var.get()

        all_users_stats = {}
        all_users = basicqueries.get_all_users()
        for user in all_users:
            user_stats = {
                "MaxQuestionsAnswered": basicqueries.get_high_score_questions(user[1]),
                "First on": basicqueries.get_date_of_high_score_questions(user[1], basicqueries.get_high_score_questions(user[1])),
                "TTTWins": basicqueries.get_outcomes(user[1],"win"),
                "TTTDraws": basicqueries.get_outcomes(user[1],"draw"),
                "TTTLosses": basicqueries.get_outcomes(user[1],"loss")
            }
            all_users_stats[user[1]] = user_stats

        if sort_criteria == "Max Questions Answered":
            sorted_users = sorted(all_users_stats.keys(), key=lambda user: all_users_stats[user]["MaxQuestionsAnswered"], reverse=True)
        elif sort_criteria == "First on":
            sorted_users = sorted(all_users_stats.keys(), key=lambda user: all_users_stats[user]["First on"], reverse=True)
        elif sort_criteria == "TTT Wins":
            sorted_users = sorted(all_users_stats.keys(), key=lambda user: all_users_stats[user]["TTTWins"], reverse=True)
        elif sort_criteria == "TTT Draws":
            sorted_users = sorted(all_users_stats.keys(), key=lambda user: all_users_stats[user]["TTTDraws"], reverse=True)
        elif sort_criteria == "TTT Losses":
            sorted_users = sorted(all_users_stats.keys(), key=lambda user: all_users_stats[user]["TTTLosses"], reverse=True)

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        for i, user in enumerate(sorted_users):
            stats = all_users_stats[user]
            bg_color = self.highlight_color if user == self.username else '#160559'

            user_label = Label(self.main_frame, text=user, font=self.title_font, bg=bg_color, fg='white', width=30, anchor="w")
            user_label.grid(row=i, column=0, sticky="ew")

            for j, (stat_name, stat_value) in enumerate(stats.items()):
                stat_label = Label(self.main_frame, text=f"{stat_name}: {stat_value}", font=self.stats_font, bg=bg_color, fg='white', width=30, anchor="w", wraplength=275)
                stat_label.grid(row=i, column=j+1, sticky="ew")

    def back_to_profile(self):
        self.root.destroy()
        profilepage.ProfilePage(self.username)

if __name__ == "__main__":
    username = "mihinka"
    app = StatisticsDisplay(username)
from tkinter import *
from database import basicqueries

def display_statistics(username):

    def sort_statistics():
        
        sort_criteria = sort_var.get()

        all_users_stats = {}
        all_users = basicqueries.get_all_users()
        for user in all_users:
            user_stats = {
                "MaxQuestionsAnswered": basicqueries.get_high_score_questions(user[1]),
                "First on": basicqueries.get_date_of_high_score_questions(user[1], basicqueries.get_high_score_questions(user[1])),
                "TTTWins": basicqueries.get_wins(user[1]),
                "TTTDraws": basicqueries.get_draws(user[1]),
                "TTTLosses": basicqueries.get_losses(user[1])
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

        for widget in main_frame.winfo_children():
            widget.destroy()

        for i, user in enumerate(sorted_users):
            stats = all_users_stats[user]
            bg_color = highlight_color if user == username else MAIN_COLOUR

            user_label = Label(main_frame, text=user, font=title_font, bg=bg_color, fg='white', width=30, anchor="w")
            user_label.grid(row=i, column=0, sticky="ew")

            for j, (stat_name, stat_value) in enumerate(stats.items()):
                stat_label = Label(main_frame, text=f"{stat_name}: {stat_value}", font=stats_font, bg=bg_color, fg='white', width=30, anchor="w", wraplength=275)
                stat_label.grid(row=i, column=j+1, sticky="ew")

    root = Tk()
    root.title("Statistics")
    root.geometry('1520x980')
    root.config(bg=MAIN_COLOUR)

    title_font = (None, 16, "bold")
    stats_font = (None, 12)
    highlight_color = OPTIONS_COLOUR

    sort_options = ["Max Questions Answered", "First on", "TTT Wins", "TTT Draws", "TTT Losses"]
    sort_var = StringVar()
    sort_var.set(sort_options[0])

    sort_label = Label(root, text="Sort By:", bg=MAIN_COLOUR, fg='white', font=title_font)
    sort_label.pack(side="top", padx=10, pady=10)

    sort_menu = OptionMenu(root, sort_var, *sort_options)
    sort_menu.config(bg=MAIN_COLOUR, fg='white', font=stats_font)
    sort_menu.pack(side="top", padx=10, pady=5)

    sort_button = Button(root, text="Sort", command=sort_statistics)
    sort_button.pack(side="top", padx=10, pady=5)

    canvas = Canvas(root, bg=MAIN_COLOUR)
    scrollbar_x = Scrollbar(root, orient="horizontal", command=canvas.xview)
    scrollbar_y = Scrollbar(root, orient="vertical", command=canvas.yview)

    main_frame = Frame(canvas, bg=MAIN_COLOUR)
    main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=main_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")

    all_users_stats = {}
    all_users = basicqueries.get_all_users()
    for user in all_users:
        user_stats = {
            "MaxQuestionsAnswered": basicqueries.get_high_score_questions(user[1]),
            "First on": basicqueries.get_date_of_high_score_questions(user[1], basicqueries.get_high_score_questions(user[1])),
            "TTTWins": basicqueries.get_wins(user[1]),
            "TTTDraws": basicqueries.get_draws(user[1]),
            "TTTLosses": basicqueries.get_losses(user[1])
        }
        all_users_stats[user[1]] = user_stats

    for i, (user, stats) in enumerate(all_users_stats.items()):
        bg_color = highlight_color if user == username else MAIN_COLOUR

        user_label = Label(main_frame, text=user, font=title_font, bg=bg_color, fg='white', width=30, anchor="w")
        user_label.grid(row=i, column=0, sticky="ew")

        for j, (stat_name, stat_value) in enumerate(stats.items()):
            stat_label = Label(main_frame, text=f"{stat_name}: {stat_value}", font=stats_font, bg=bg_color, fg='white', width=30, anchor="w", wraplength=275)
            stat_label.grid(row=i, column=j+1, sticky="ew")

    canvas.pack(side="left", fill="both", expand=True)

    root.mainloop()

MAIN_COLOUR = '#160559'
OPTIONS_COLOUR = '#ffb300'

username = "mihinka"
display_statistics(username)

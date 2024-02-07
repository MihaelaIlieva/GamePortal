from tkinter import *
from tkinter import messagebox
import profilepage
from database import basicqueries
import random

current_question = ""
questions_answered = 0
easy_questions = []
medium_questions = []
hard_questions = []

def create_main_window():
    root = Tk()
    root.geometry('1520x980')
    root.title("Who wants to be a millionaire")
    root.config(bg=MAIN_COLOUR)
    return root

def create_game_frame(root):
    game_frame = Frame(root, bg=MAIN_COLOUR, padx=120)
    game_frame.grid(row=0, column=0)
    return game_frame

def create_hints_frame(game_frame):
    hints_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
    hints_frame.grid(row=0, column=0)

    public_button = Button(hints_frame, image=unused_public, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1')
    public_button.grid(row=0, column=0, padx=10)

    fiftyfifty_button = Button(hints_frame, image=unused_fiftyfifty, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1')
    fiftyfifty_button.grid(row=0, column=1, padx=10)

    callafriend_button = Button(hints_frame, image=unused_callafriend, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1')
    callafriend_button.grid(row=0, column=2, padx=10)
    return hints_frame

def create_logo_frame(game_frame):
    logo_frame = Frame(game_frame, bg=MAIN_COLOUR)
    logo_frame.grid(row=1, column=0)
    logo_frame_label = Label(logo_frame, image=logo_picture, bg=MAIN_COLOUR, bd=0, width = 950, height=450)
    logo_frame_label.grid(row=0, column=0)
    return logo_frame

def create_questions_frame(game_frame, first_question_package):
    global current_question, questions_answered
    questions_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
    questions_frame.grid(row=2, column=0)
    questions_frame_label = Label(questions_frame, image=question_picture, bg=MAIN_COLOUR, width = 950, height=300)
    questions_frame_label.grid(row=0, column=0)

    #TODO: make it fit in the question bubble and don't forget to disable the writing of the user
    question = Text(questions_frame, font=(None,20), width=49, height=2.50, bg=QUESTIONS_COLOUR, bd=0, wrap="word", state="normal", fg="white")
    question.place(x=100, y=8.50)
    question.insert("1.0", first_question_package[1])
    question.config(state="disabled")

    current_question = first_question_package[1]

    first_label = Label(questions_frame, font=(None,16), text='А: ', bg=QUESTIONS_COLOUR, fg=OPTIONS_COLOUR)
    first_label.place(x=80, y=150)
    second_label = Label(questions_frame, font=(None,16), text='Б: ', bg=QUESTIONS_COLOUR, fg=OPTIONS_COLOUR)
    second_label.place(x=520, y=150)
    third_label = Label(questions_frame, font=(None,16), text='В: ', bg=QUESTIONS_COLOUR, fg=OPTIONS_COLOUR)
    third_label.place(x=80, y=230)
    fourth_label = Label(questions_frame, font=(None,16), text='Г: ', bg=QUESTIONS_COLOUR, fg=OPTIONS_COLOUR)
    fourth_label.place(x=520, y=230)

    answers = [first_question_package[2], first_question_package[3], first_question_package[4], first_question_package[5]]
    random.shuffle(answers)

    first_button = Button(questions_frame, text=answers[0], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    first_button.place(x=130, y=145)
    first_button.bind('<ButtonRelease-1>', mark_answer)
    # first_button.bind('<Enter>', change_letter_colour(first_label, 'white'))
    # first_button.bind('<Leave>', change_letter_colour(first_label, OPTIONS_COLOUR))

    second_button = Button(questions_frame, text=answers[1], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    second_button.place(x=570, y=145)
    second_button.bind('<ButtonRelease-1>', mark_answer)

    third_button = Button(questions_frame, text=answers[2], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    third_button.place(x=130, y=225)
    third_button.bind('<ButtonRelease-1>', mark_answer)

    fourth_button = Button(questions_frame, text=answers[3], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    fourth_button.place(x=570, y=225)
    fourth_button.bind('<ButtonRelease-1>', mark_answer)

    number_of_question = Label(questions_frame, text=str(questions_answered+1), font=(None, 16, 'bold'), bg=MAIN_COLOUR, fg='white', width=4, height=2)
    number_of_question.place(x=447, y=177.5)
    return questions_frame

def create_money_frame(root):
    money_frame = Frame(root, bg=MAIN_COLOUR, padx=55, pady=45)
    money_frame.grid(row=0, column=1)
    money_frame_label = Label(money_frame, image=first_sum, bg=MAIN_COLOUR, width=250, height=750)
    money_frame_label.grid(row=0, column=0)
    return money_frame

#TODO: implement it
def on_button_click(button_number):
    reset_timer()
    print(f"Button {button_number} clicked!")

def reset_timer():
    global timer_seconds
    timer_seconds = TIMER_DURATION
    update_timer()

def show_timeout_popup():
    choice = messagebox.askquestion("Time's Up!", "Do you want to start a new game?", icon='warning')
    if choice == 'yes':
        #TODO: Add logic to reset the game or navigate to the new game
        # reset_game()
        reset_timer()
    else:
        root.destroy()
        profilepage.ProfilePage()
        

def update_timer():
    global timer_seconds, easy_questions, medium_questions, hard_questions
    timer_label.config(text=f"Time left: {timer_seconds} seconds")
    if timer_seconds > 0:
        timer_seconds -= 1
        root.after(1000, update_timer)
    else:
        show_timeout_popup()

def get_new_question():
    global questions_answered
    if questions_answered < 5:
        new_question = easy_questions[questions_answered]
    elif questions_answered >= 5 and questions_answered < 10:
        new_question = medium_questions[questions_answered-5]
    else:
        new_question = hard_questions[questions_answered-10]
    create_questions_frame(game_frame, new_question)


def mark_answer(event):
    global questions_answered

    button_marked = event.widget
    button_answer = button_marked['text']
    correct_answer = basicqueries.get_correct_answer(current_question)[0][0]
    if button_answer == correct_answer:
        print("Correct!")
        questions_answered += 1
        if questions_answered < 15:
            get_new_question()
        else:
            pass
            # win_game()
    else:
        print("Incorrect!")
        pass
        # lose_game()
        # save_progress()
        # open_profile_page()

    print("Hello, {button}".format(button = button_answer))

def change_letter_colour(changing_object, colour):
    changing_object.config(fg=colour)

if __name__ == "__main__":

    MAIN_COLOUR = '#160559'
    QUESTIONS_COLOUR = '#233e91'
    OPTIONS_COLOUR = '#ffb300'
    TIMER_DURATION = 60

    questions_answered = 0

    easy_questions = basicqueries.get_questions_by_difficulty("easy")
    medium_questions = basicqueries.get_questions_by_difficulty("medium")
    hard_questions = basicqueries.get_questions_by_difficulty("hard")
    random.shuffle(easy_questions)
    random.shuffle(medium_questions)
    random.shuffle(hard_questions)
    first_question_package = easy_questions[len(easy_questions)-1]
    
    root = create_main_window()
    
    #Unused hints
    unused_public = PhotoImage(file='images/public.png')
    unused_fiftyfifty = PhotoImage(file='images/fiftyfifty.png')
    unused_callafriend = PhotoImage(file='images/callafriend.png')

    #Used hints
    used_public = PhotoImage(file='images/publiccr.png')
    used_fiftyfifty = PhotoImage(file='images/fiftyfiftycr.png')
    used_callafriend = PhotoImage(file='images/callafriendcr.png')

    #Main picture
    logo_picture = PhotoImage(file='images/mainpicture.png')

    #Money scale pictures
    first_sum = PhotoImage(file='images/sb1.png')
    second_sum = PhotoImage(file='images/sb2.png')
    third_sum = PhotoImage(file='images/sb3.png')
    fourth_sum = PhotoImage(file='images/sb4.png')
    fifth_sum = PhotoImage(file='images/sb5.png')
    sixth_sum = PhotoImage(file='images/sb6.png')
    seventh_sum = PhotoImage(file='images/sb7.png')
    eight_sum = PhotoImage(file='images/sb8.png')
    ninght_sum = PhotoImage(file='images/sb9.png')
    tenth_sum = PhotoImage(file='images/sb10.png')
    eleventh_sum = PhotoImage(file='images/sb11.png')
    twelfth_sum = PhotoImage(file='images/sb12.png')
    thirteenth_sum = PhotoImage(file='images/sb13.png')
    fourteenth_sum = PhotoImage(file='images/sb14.png')
    fifteenth_sum = PhotoImage(file='images/sb15.png')

    #Question options picture
    question_picture = PhotoImage(file='images/question.png')
    
    game_frame = create_game_frame(root)
    hints_frame = create_hints_frame(game_frame)
    logo_frame = create_logo_frame(game_frame)
    questions_frame = create_questions_frame(game_frame, first_question_package)
    money_frame = create_money_frame(root)

    timer_seconds = TIMER_DURATION
    timer_label = Label(root, text=f"Time left: {timer_seconds} seconds", font=(None, 16), bg=MAIN_COLOUR, fg="white")
    timer_label.grid(row=1, column=0, pady=10)

    reset_timer()

    root.mainloop()
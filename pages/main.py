from tkinter import *
from tkinter import messagebox
import profilepage
from database import basicqueries
import random
from tkinter.ttk import Progressbar
import openai
import datetime

current_question = ""
first_answer = ""
second_answer = ""
third_answer = ""
fourth_answer = ""
questions_answered = 0
new_root = None
public_button = None
fiftyfifty_button = None
first_button = None
second_button = None
third_button = None
fourth_button = None
callafriend_button = None
input_window = None
username = "mihinka123"
password = ""
#Removed from here for safety reasons
openai.api_key = 'my_api_key'

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
    global public_button, fiftyfifty_button, callafriend_button
    hints_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
    hints_frame.grid(row=0, column=0)

    public_button = Button(hints_frame, image=unused_public, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1', command=use_public)
    public_button.grid(row=0, column=0, padx=10)

    fiftyfifty_button = Button(hints_frame, image=unused_fiftyfifty, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1', command=use_fifty_fifty)
    fiftyfifty_button.grid(row=0, column=1, padx=10)

    callafriend_button = Button(hints_frame, image=unused_callafriend, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65, cursor='hand1', command=use_call_a_friend)
    callafriend_button.grid(row=0, column=2, padx=10)
    return hints_frame

def create_logo_frame(game_frame):
    logo_frame = Frame(game_frame, bg=MAIN_COLOUR)
    logo_frame.grid(row=1, column=0)
    logo_frame_label = Label(logo_frame, image=logo_picture, bg=MAIN_COLOUR, bd=0, width = 950, height=450)
    logo_frame_label.grid(row=0, column=0)
    return logo_frame

def create_questions_frame(game_frame, first_question_package):
    global current_question, questions_answered, first_answer, second_answer, third_answer, fourth_answer, first_button, second_button, third_button, fourth_button
    questions_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
    questions_frame.grid(row=2, column=0)
    questions_frame_label = Label(questions_frame, image=question_picture, bg=MAIN_COLOUR, width = 950, height=300)
    questions_frame_label.grid(row=0, column=0)

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
    first_answer = answers[0]

    second_button = Button(questions_frame, text=answers[1], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    second_button.place(x=570, y=145)
    second_button.bind('<ButtonRelease-1>', mark_answer)
    second_answer = answers[1]

    third_button = Button(questions_frame, text=answers[2], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    third_button.place(x=130, y=225)
    third_button.bind('<ButtonRelease-1>', mark_answer)
    third_answer = answers[2]

    fourth_button = Button(questions_frame, text=answers[3], font=(None,16), bd=0, bg=QUESTIONS_COLOUR, fg='white', activebackground=QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
    fourth_button.place(x=570, y=225)
    fourth_button.bind('<ButtonRelease-1>', mark_answer)
    fourth_answer = answers[3]

    number_of_question = Label(questions_frame, text=str(questions_answered+1), font=(None, 16, 'bold'), bg=MAIN_COLOUR, fg='white', width=4, height=2)
    number_of_question.place(x=447, y=177.5)
    return questions_frame

def create_money_frame(root, image_sum):
    money_frame = Frame(root, bg=MAIN_COLOUR, padx=125, pady=45)
    money_frame.grid(row=0, column=1)
    money_frame_label = Label(money_frame, image=image_sum, bg=MAIN_COLOUR, width=275, height=750)
    money_frame_label.grid(row=0, column=0)
    return money_frame

def remove_public_answers():
    first_progress_bar.place_forget()
    second_progress_bar.place_forget()
    third_progress_bar.place_forget()
    fourth_progress_bar.place_forget()
    first_bar_label.place_forget()
    second_bar_label.place_forget()
    third_bar_label.place_forget()
    fourth_bar_label.place_forget()

def get_correct_option():
    global current_question, first_answer, second_answer, third_answer, fourth_answer
    correct_answer = basicqueries.get_correct_answer(current_question)[0][0]
    if  first_answer == correct_answer:
        return "А"
    elif second_answer == correct_answer:
        return "Б"
    elif third_answer ==correct_answer:
        return "В"
    else:
        return "Г"
    
def get_random_percentages():
    first_number = random.randint(0,24)
    second_number = random.randint(0,24)
    third_number = random.randint(0,24)
    fourth_number = 100 - (first_number + second_number + third_number)
    return first_number, second_number, third_number, fourth_number

def chat_with_gpt(prompt):
    model_name = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You: " + prompt},
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

def use_public():
    global public_button
    public_button.config(state='disabled', image=used_public)
    first_progress_bar.place(x=1000, y=350)
    second_progress_bar.place(x=1045, y=350)
    third_progress_bar.place(x=1090, y=350)
    fourth_progress_bar.place(x=1135, y=350)
    
    first_bar_label.place(x=1000, y=475)
    second_bar_label.place(x=1045, y=475)
    third_bar_label.place(x=1090, y=475)
    fourth_bar_label.place(x=1135, y=475)

    first_number, second_number, third_number, max_percentages = get_random_percentages()

    correct_option = get_correct_option()
    if correct_option == "А":
        first_bar_label.config(text="А: {max_percentages}%".format(max_percentages=max_percentages))
        second_bar_label.config(text="Б: {first_number}%".format(first_number=first_number))
        third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
        fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

        first_progress_bar.config(value=max_percentages)
        second_progress_bar.config(value=first_number)
        third_progress_bar.config(value=second_number)
        fourth_progress_bar.config(value=third_number)

    elif correct_option == "Б":
        second_bar_label.config(text="Б: {max_percentages}%".format(max_percentages=max_percentages))
        first_bar_label.config(text="А: {first_number}%".format(first_number=first_number))
        third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
        fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

        first_progress_bar.config(value=first_number)
        second_progress_bar.config(value=max_percentages)
        third_progress_bar.config(value=second_number)
        fourth_progress_bar.config(value=third_number)

    elif correct_option == "В":
        third_bar_label.config(text="В: {max_percentages}%".format(max_percentages=max_percentages))
        first_bar_label.config(text="А: {first_number}%".format(first_number=first_number))
        second_bar_label.config(text="Б: {second_number}%".format(second_number=second_number))
        fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

        first_progress_bar.config(value=first_number)
        second_progress_bar.config(value=second_number)
        third_progress_bar.config(value=max_percentages)
        fourth_progress_bar.config(value=third_number)

    else:
        fourth_bar_label.config(text="Г: {max_percentages}%".format(max_percentages=max_percentages))
        second_bar_label.config(text="Б: {first_number}%".format(first_number=first_number))
        third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
        first_bar_label.config(text="А: {third_number}%".format(third_number=third_number))

        first_progress_bar.config(value=third_number)
        second_progress_bar.config(value=first_number)
        third_progress_bar.config(value=second_number)
        fourth_progress_bar.config(value=max_percentages)

def use_fifty_fifty():
    global fiftyfifty_button, first_button, second_button, third_button, fourth_button
    fiftyfifty_button.config(state='disabled', image=used_fiftyfifty)
    options_to_eliminate = []
    correct_option = get_correct_option()

    if correct_option == "А":
        options_to_eliminate = random.sample([2,3,4], 2)

    elif correct_option == "Б":
        options_to_eliminate = random.sample([1,3,4], 2)

    elif correct_option == "В":
        options_to_eliminate = random.sample([1,2,4], 2)

    else:
        options_to_eliminate = random.sample([1,2,3], 2)
    
    if 1 in options_to_eliminate:
        first_button.config(state='disabled', text="")
    if 2 in options_to_eliminate:
        second_button.config( state='disabled', text="")
    if 3 in options_to_eliminate:
        third_button.config(state='disabled', text="")
    if 4 in options_to_eliminate:
        fourth_button.config(state='disabled', text="")

def use_call_a_friend():
    global callafriend_button, input_window
    callafriend_button.config(state='disabled', image=used_callafriend)
    def get_response():
        user_question = question_entry.get()
        try:
            response = chat_with_gpt(user_question)
            response_text.config(state='normal')
            response_text.insert("1.0", "")
            response_text.insert("1.0", response)
            response_text.config(state='disabled')

        except openai.error.RateLimitError:
            response_text.config(state='normal')
            response_text.insert("1.0", "")
            response_text.insert("1.0", "API rate limit exceeded. Please try again later.")
            response_text.config(state='disabled')

    input_window = Toplevel(root)
    input_window.title("Помощ от приятел")
    input_window.geometry('700x350+500+235')
    input_window.config(bg='white')
    input_window.overrideredirect(True)
    
    label = Label(input_window, text = "Помощ от приятел", font=(None, 16), width=35, height=3, bg='white', bd=0, fg='black')
    label.pack()

    question_entry = Entry(input_window, width=50)
    question_entry.pack(pady=10)

    submit_button = Button(input_window, text="Попитай", command=get_response)
    submit_button.pack(pady=10)

    response_text = Text(input_window, font=(None,12), width=35, height=15, bd=0, wrap="word", state="disabled", fg="black")
    response_text.pack()

    input_window.mainloop()

def reset_timer():
    global timer_seconds
    if hasattr(root, 'timer_id'):
        root.after_cancel(root.timer_id)
    timer_seconds = TIMER_DURATION
    update_timer()

def show_timeout_popup():
    choice = messagebox.askquestion("Time's Up!", "Do you want to start a new game?", icon='warning')
    if choice == 'yes':
        #TODO: Add logic to reset the game or navigate to the new game
        try_again()
    else:
        root.destroy()
        profilepage.ProfilePage()      

def update_timer():
    global timer_seconds
    timer_label.config(text=f"Time left: {timer_seconds} seconds")
    if timer_seconds > 0:
        timer_seconds -= 1
        root.timer_id = root.after(1000, update_timer)
    else:
        show_timeout_popup()

def stop_timer():
    if hasattr(root, 'timer_id'):
        root.after_cancel(root.timer_id)

def get_new_question():
    global questions_answered
    if questions_answered < 5:
        new_question = easy_questions[questions_answered]
    elif questions_answered >= 5 and questions_answered < 10:
        new_question = medium_questions[questions_answered-5]
    else:
        new_question = hard_questions[questions_answered-10]
    create_questions_frame(game_frame, new_question)

def change_money_picture():
    global questions_answered
    match questions_answered:
        case 0:
            image = first_sum
        case 1:
            image = second_sum
        case 2:
            image = third_sum
        case 3:
            image = fourth_sum
        case 4:
            image = fifth_sum
        case 5:
            image = sixth_sum
        case 6:
            image = seventh_sum
        case 7:
            image = eight_sum
        case 8:
            image = ninght_sum
        case 9:
            image = tenth_sum
        case 10:
            image = eleventh_sum
        case 11:
            image = twelfth_sum
        case 12:
            image = thirteenth_sum
        case 13:
            image = fourteenth_sum
        case 14:
            image = fifteenth_sum
    create_money_frame(root, image)

def try_again():
    global questions_answered, easy_questions, new_root, public_button, fiftyfifty_button, callafriend_button
    public_button.config(state='normal', image=unused_public)
    fiftyfifty_button.config(state='normal', image=unused_fiftyfifty)
    callafriend_button.config(state='normal', image=unused_callafriend)
    questions_answered = 0
    random.shuffle(easy_questions)
    random.shuffle(medium_questions)
    random.shuffle(hard_questions)
    reset_timer()
    new_question_package = easy_questions[len(easy_questions)-1]
    create_questions_frame(game_frame, new_question_package)
    create_money_frame(root, first_sum)
    if new_root:
        new_root.destroy()

def back_to_profile():
    #TODO: redirect to profilepage
    root.destroy()
    pass

def game_over():
    global new_root
    #TODO: add result to database

    stop_timer()
    new_root = Toplevel()
    new_root.config(bg=WRONG_ANSWER_COLOUR)
    new_root.geometry('375x325+600+350')
    new_root.title("Game over")
    new_root.overrideredirect(True)
    losing_message = Label(new_root, image=losing_picture, bd=0)
    losing_message.pack()

    try_again_button = Button(new_root, text="Нова игра", font=(None,16,'bold'), bg=WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=try_again)
    try_again_button.pack()
    back_to_profile_button = Button(new_root, text="Към профила ми", font=(None,16,'bold'), bg=WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=back_to_profile)
    back_to_profile_button.pack()

def win_game():
    global new_root
    #TODO: add result to database

    stop_timer()
    new_root = Toplevel()
    new_root.config(bg=WRONG_ANSWER_COLOUR)
    new_root.geometry('525x625+600+235')
    new_root.title("Game won")
    losing_message = Label(new_root, image=winning_picture, bd=0)
    losing_message.pack()

    try_again_button = Button(new_root, text="Нова игра", font=(None,16,'bold'), bg=WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=try_again)
    try_again_button.pack()
    back_to_profile_button = Button(new_root, text="Към профила ми", font=(None,16,'bold'), bg=WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=back_to_profile)
    back_to_profile_button.pack()

def save_progress():
    # add_played_game(username, game_name, date_played, questions_answered, outcome)
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    basicqueries.add_played_game(username, "become_rich", current_date, questions_answered, "none")

def mark_answer(event):
    global questions_answered, input_window
    remove_public_answers()
    
    if input_window != None:
        input_window.destroy()
    button_marked = event.widget
    if button_marked['state'] != 'disabled':
        button_answer = button_marked['text']
        correct_answer = basicqueries.get_correct_answer(current_question)[0][0]
        if button_answer == correct_answer:
            print("Correct!")
            questions_answered += 1
            if questions_answered < 15:
                reset_timer()
                change_money_picture()
                get_new_question()
            else:
                save_progress()
                win_game()
        else:
            print("Incorrect!")
            save_progress()
            game_over()
            # open_profile_page()
    else:
        pass

    #print("Hello, {button}".format(button = button_answer))

if __name__ == "__main__":

    MAIN_COLOUR = '#160559'
    QUESTIONS_COLOUR = '#233e91'
    OPTIONS_COLOUR = '#ffb300'
    WRONG_ANSWER_COLOUR = '#101248'
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

    #States pictures
    winning_picture = PhotoImage(file='images/winning.png')
    losing_picture = PhotoImage(file='images/losing.png')
    
    game_frame = create_game_frame(root)
    hints_frame = create_hints_frame(game_frame)
    logo_frame = create_logo_frame(game_frame)
    questions_frame = create_questions_frame(game_frame, first_question_package)
    money_frame = create_money_frame(root, first_sum)

    timer_seconds = TIMER_DURATION
    timer_label = Label(root, text=f"Time left: {timer_seconds} seconds", font=(None, 16), bg=MAIN_COLOUR, fg="white")
    timer_label.grid(row=1, column=0, pady=10)

    first_progress_bar = Progressbar(root, orient=VERTICAL, length=100)
    second_progress_bar = Progressbar(root, orient=VERTICAL, length=100)
    third_progress_bar = Progressbar(root, orient=VERTICAL, length=100)
    fourth_progress_bar = Progressbar(root, orient=VERTICAL, length=100)

    first_bar_label = Label(root, text="А", font=(None,10), bg=MAIN_COLOUR, fg='white')
    second_bar_label = Label(root, text="Б", font=(None,10), bg=MAIN_COLOUR, fg='white')
    third_bar_label = Label(root, text="В", font=(None,10), bg=MAIN_COLOUR, fg='white')
    fourth_bar_label = Label(root, text="Г", font=(None,10), bg=MAIN_COLOUR, fg='white')

    reset_timer()

    root.mainloop()
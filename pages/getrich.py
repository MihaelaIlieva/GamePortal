import openai
import random
import datetime
import profilepage
from database import basicqueries
from tkinter.ttk import Progressbar
from tkinter import Tk, Frame, Button, Label, Text, Entry, messagebox, PhotoImage, Toplevel, VERTICAL

class GetRichGame:

    def __init__(self, username):
        self.username = username

        self.current_question = ""
        self.first_answer = ""
        self.second_answer = ""
        self.third_answer = ""
        self.fourth_answer = ""
        self.questions_answered = 0
        self.new_root = None
        self.public_button = None
        self.fiftyfifty_button = None
        self.first_button = None
        self.second_button = None
        self.third_button = None
        self.fourth_button = None
        self.callafriend_button = None
        self.input_window = None
        #Removed from here for safety reasons
        openai.api_key = 'my_api_key'

        self.MAIN_COLOUR = '#160559'
        self.QUESTIONS_COLOUR = '#233e91'
        self.OPTIONS_COLOUR = '#ffb300'
        self.WRONG_ANSWER_COLOUR = '#101248'
        self.TIMER_DURATION = 60

        self.questions_answered = 0

        self.easy_questions = basicqueries.get_questions_by_difficulty("easy")
        self.medium_questions = basicqueries.get_questions_by_difficulty("medium")
        self.hard_questions = basicqueries.get_questions_by_difficulty("hard")
        random.shuffle(self.easy_questions)
        random.shuffle(self.medium_questions)
        random.shuffle(self.hard_questions)
        self.first_question_package = self.easy_questions[len(self.easy_questions)-1]

        self.root = self.create_main_window()

        #Unused hints
        self.unused_public = PhotoImage(file='images/public.png')
        self.unused_fiftyfifty = PhotoImage(file='images/fiftyfifty.png')
        self.unused_callafriend = PhotoImage(file='images/callafriend.png')

        #Used hints
        self.used_public = PhotoImage(file='images/publiccr.png')
        self.used_fiftyfifty = PhotoImage(file='images/fiftyfiftycr.png')
        self.used_callafriend = PhotoImage(file='images/callafriendcr.png')

        #Main picture
        self.logo_picture = PhotoImage(file='images/mainpicture.png')

        #Money scale pictures
        self.first_sum = PhotoImage(file='images/sb1.png')
        self.second_sum = PhotoImage(file='images/sb2.png')
        self.third_sum = PhotoImage(file='images/sb3.png')
        self.fourth_sum = PhotoImage(file='images/sb4.png')
        self.fifth_sum = PhotoImage(file='images/sb5.png')
        self.sixth_sum = PhotoImage(file='images/sb6.png')
        self.seventh_sum = PhotoImage(file='images/sb7.png')
        self.eight_sum = PhotoImage(file='images/sb8.png')
        self.ninght_sum = PhotoImage(file='images/sb9.png')
        self.tenth_sum = PhotoImage(file='images/sb10.png')
        self.eleventh_sum = PhotoImage(file='images/sb11.png')
        self.twelfth_sum = PhotoImage(file='images/sb12.png')
        self.thirteenth_sum = PhotoImage(file='images/sb13.png')
        self.fourteenth_sum = PhotoImage(file='images/sb14.png')
        self.fifteenth_sum = PhotoImage(file='images/sb15.png')

        #Question options picture
        self.question_picture = PhotoImage(file='images/question.png')

        #States pictures
        self.winning_picture = PhotoImage(file='images/winning.png')
        self.losing_picture = PhotoImage(file='images/losing.png')

        self.game_frame = self.create_game_frame(self.root)
        self.hints_frame = self.create_hints_frame(self.game_frame)
        self.logo_frame = self.create_logo_frame(self.game_frame)
        self.questions_frame = self.create_questions_frame(self.game_frame, self.first_question_package)
        self.money_frame = self.create_money_frame(self.root, self.first_sum)

        self.timer_seconds = self.TIMER_DURATION
        self.timer_label = Label(self.root, text=f"Time left: {self.timer_seconds} seconds", font=(None, 16), bg=self.MAIN_COLOUR, fg="white")
        self.timer_label.grid(row=1, column=0, pady=10)

        self.first_progress_bar = Progressbar(self.root, orient=VERTICAL, length=100)
        self.second_progress_bar = Progressbar(self.root, orient=VERTICAL, length=100)
        self.third_progress_bar = Progressbar(self.root, orient=VERTICAL, length=100)
        self.fourth_progress_bar = Progressbar(self.root, orient=VERTICAL, length=100)

        self.first_bar_label = Label(self.root, text="А", font=(None,10), bg=self.MAIN_COLOUR, fg='white')
        self.second_bar_label = Label(self.root, text="Б", font=(None,10), bg=self.MAIN_COLOUR, fg='white')
        self.third_bar_label = Label(self.root, text="В", font=(None,10), bg=self.MAIN_COLOUR, fg='white')
        self.fourth_bar_label = Label(self.root, text="Г", font=(None,10), bg=self.MAIN_COLOUR, fg='white')

        self.reset_timer()

        self.root.mainloop()

    def get_username(self):
        return self.username
    
    def create_main_window(self):
        self.root = Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Who wants to be a millionaire")
        self.root.config(bg=self.MAIN_COLOUR)
        return self.root

    def create_game_frame(self, root):
        self.game_frame = Frame(root, bg=self.MAIN_COLOUR, padx=120)
        self.game_frame.grid(row=0, column=0)
        return self.game_frame

    def create_hints_frame(self, game_frame):
        self.hints_frame = Frame(game_frame, bg=self.MAIN_COLOUR, pady=35)
        self.hints_frame.grid(row=0, column=0)

        self.public_button = Button(self.hints_frame, image=self.unused_public, bg=self.MAIN_COLOUR, bd=0.5, activebackground=self.MAIN_COLOUR, width=110, height=65, cursor='hand1', command=self.use_public)
        self.public_button.grid(row=0, column=0, padx=10)

        self.fiftyfifty_button = Button(self.hints_frame, image=self.unused_fiftyfifty, bg=self.MAIN_COLOUR, bd=0.5, activebackground=self.MAIN_COLOUR, width=110, height=65, cursor='hand1', command=self.use_fifty_fifty)
        self.fiftyfifty_button.grid(row=0, column=1, padx=10)

        self.callafriend_button = Button(self.hints_frame, image=self.unused_callafriend, bg=self.MAIN_COLOUR, bd=0.5, activebackground=self.MAIN_COLOUR, width=110, height=65, cursor='hand1', command=self.use_call_a_friend)
        self.callafriend_button.grid(row=0, column=2, padx=10)
        return self.hints_frame

    def create_logo_frame(self, game_frame):
        self.logo_frame = Frame(game_frame, bg=self.MAIN_COLOUR)
        self.logo_frame.grid(row=1, column=0)
        self.logo_frame_label = Label(self.logo_frame, image=self.logo_picture, bg=self.MAIN_COLOUR, bd=0, width = 950, height=450)
        self.logo_frame_label.grid(row=0, column=0)
        return self.logo_frame

    def create_questions_frame(self, game_frame, first_question_package):
        self.questions_frame = Frame(game_frame, bg=self.MAIN_COLOUR, pady=35)
        self.questions_frame.grid(row=2, column=0)
        self.questions_frame_label = Label(self.questions_frame, image=self.question_picture, bg=self.MAIN_COLOUR, width = 950, height=300)
        self.questions_frame_label.grid(row=0, column=0)

        self.question = Text(self.questions_frame, font=(None,20), width=49, height=2.50, bg=self.QUESTIONS_COLOUR, bd=0, wrap="word", state="normal", fg="white")
        self.question.place(x=100, y=8.50)
        self.question.insert("1.0", first_question_package[1])
        self.question.config(state="disabled")

        self.current_question = first_question_package[1]

        self.first_label = Label(self.questions_frame, font=(None,16), text='А: ', bg=self.QUESTIONS_COLOUR, fg=self.OPTIONS_COLOUR)
        self.first_label.place(x=80, y=150)
        self.second_label = Label(self.questions_frame, font=(None,16), text='Б: ', bg=self.QUESTIONS_COLOUR, fg=self.OPTIONS_COLOUR)
        self.second_label.place(x=520, y=150)
        self.third_label = Label(self.questions_frame, font=(None,16), text='В: ', bg=self.QUESTIONS_COLOUR, fg=self.OPTIONS_COLOUR)
        self.third_label.place(x=80, y=230)
        self.fourth_label = Label(self.questions_frame, font=(None,16), text='Г: ', bg=self.QUESTIONS_COLOUR, fg=self.OPTIONS_COLOUR)
        self.fourth_label.place(x=520, y=230)

        self.answers = [first_question_package[2], first_question_package[3], first_question_package[4], first_question_package[5]]
        random.shuffle(self.answers)

        self.first_button = Button(self.questions_frame, text=self.answers[0], font=(None,16), bd=0, bg=self.QUESTIONS_COLOUR, fg='white', activebackground=self.QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
        self.first_button.place(x=130, y=145)
        self.first_button.bind('<ButtonRelease-1>', self.mark_answer)
        self.first_answer = self.answers[0]

        self.second_button = Button(self.questions_frame, text=self.answers[1], font=(None,16), bd=0, bg=self.QUESTIONS_COLOUR, fg='white', activebackground=self.QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
        self.second_button.place(x=570, y=145)
        self.second_button.bind('<ButtonRelease-1>', self.mark_answer)
        self.second_answer = self.answers[1]

        self.third_button = Button(self.questions_frame, text=self.answers[2], font=(None,16), bd=0, bg=self.QUESTIONS_COLOUR, fg='white', activebackground=self.QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
        self.third_button.place(x=130, y=225)
        self.third_button.bind('<ButtonRelease-1>', self.mark_answer)
        self.third_answer = self.answers[2]

        self.fourth_button = Button(self.questions_frame, text=self.answers[3], font=(None,16), bd=0, bg=self.QUESTIONS_COLOUR, fg='white', activebackground=self.QUESTIONS_COLOUR, activeforeground='white', cursor='hand1')
        self.fourth_button.place(x=570, y=225)
        self.fourth_button.bind('<ButtonRelease-1>', self.mark_answer)
        self.fourth_answer = self.answers[3]

        self.number_of_question = Label(self.questions_frame, text=str(self.questions_answered+1), font=(None, 16, 'bold'), bg=self.MAIN_COLOUR, fg='white', width=4, height=2)
        self.number_of_question.place(x=447, y=177.5)
        return self.questions_frame

    def create_money_frame(self, root, image_sum):
        self.money_frame = Frame(root, bg=self.MAIN_COLOUR, padx=125, pady=45)
        self.money_frame.grid(row=0, column=1)
        self.money_frame_label = Label(self.money_frame, image=image_sum, bg=self.MAIN_COLOUR, width=275, height=750)
        self.money_frame_label.grid(row=0, column=0)
        return self.money_frame

    def remove_public_answers(self):
        self.first_progress_bar.place_forget()
        self.second_progress_bar.place_forget()
        self.third_progress_bar.place_forget()
        self.fourth_progress_bar.place_forget()
        self.first_bar_label.place_forget()
        self.second_bar_label.place_forget()
        self.third_bar_label.place_forget()
        self.fourth_bar_label.place_forget()

    def get_correct_option(self):
        correct_answer = basicqueries.get_correct_answer(self.current_question)[0][0]
        if  self.first_answer == correct_answer:
            return "А"
        elif self.second_answer == correct_answer:
            return "Б"
        elif self.third_answer == correct_answer:
            return "В"
        else:
            return "Г"
        
    def get_random_percentages(self):
        self.first_number = random.randint(0,24)
        self.second_number = random.randint(0,24)
        self.third_number = random.randint(0,24)
        self.fourth_number = 100 - (self.first_number + self.second_number + self.third_number)
        return self.first_number, self.second_number, self.third_number, self.fourth_number

    def chat_with_gpt(self, prompt):
        model_name = "gpt-3.5-turbo"

        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You: " + prompt},
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']

    def use_public(self):
        self.public_button.config(state='disabled', image=self.used_public)
        self.first_progress_bar.place(x=1000, y=350)
        self.second_progress_bar.place(x=1045, y=350)
        self.third_progress_bar.place(x=1090, y=350)
        self.fourth_progress_bar.place(x=1135, y=350)
        
        self.first_bar_label.place(x=1000, y=475)
        self.second_bar_label.place(x=1045, y=475)
        self.third_bar_label.place(x=1090, y=475)
        self.fourth_bar_label.place(x=1135, y=475)

        first_number, second_number, third_number, max_percentages = self.get_random_percentages()

        correct_option = self.get_correct_option()
        if correct_option == "А":
            self.first_bar_label.config(text="А: {max_percentages}%".format(max_percentages=max_percentages))
            self.second_bar_label.config(text="Б: {first_number}%".format(first_number=first_number))
            self.third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
            self.fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

            self.first_progress_bar.config(value=max_percentages)
            self.second_progress_bar.config(value=first_number)
            self.third_progress_bar.config(value=second_number)
            self.fourth_progress_bar.config(value=third_number)

        elif correct_option == "Б":
            self.second_bar_label.config(text="Б: {max_percentages}%".format(max_percentages=max_percentages))
            self.first_bar_label.config(text="А: {first_number}%".format(first_number=first_number))
            self.third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
            self.fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

            self.first_progress_bar.config(value=first_number)
            self.second_progress_bar.config(value=max_percentages)
            self.third_progress_bar.config(value=second_number)
            self.fourth_progress_bar.config(value=third_number)

        elif correct_option == "В":
            self.third_bar_label.config(text="В: {max_percentages}%".format(max_percentages=max_percentages))
            self.first_bar_label.config(text="А: {first_number}%".format(first_number=first_number))
            self.second_bar_label.config(text="Б: {second_number}%".format(second_number=second_number))
            self.fourth_bar_label.config(text="Г: {third_number}%".format(third_number=third_number))

            self.first_progress_bar.config(value=first_number)
            self.second_progress_bar.config(value=second_number)
            self.third_progress_bar.config(value=max_percentages)
            self.fourth_progress_bar.config(value=third_number)

        else:
            self.fourth_bar_label.config(text="Г: {max_percentages}%".format(max_percentages=max_percentages))
            self.second_bar_label.config(text="Б: {first_number}%".format(first_number=first_number))
            self.third_bar_label.config(text="В: {second_number}%".format(second_number=second_number))
            self.first_bar_label.config(text="А: {third_number}%".format(third_number=third_number))

            self.first_progress_bar.config(value=third_number)
            self.second_progress_bar.config(value=first_number)
            self.third_progress_bar.config(value=second_number)
            self.fourth_progress_bar.config(value=max_percentages)

    def use_fifty_fifty(self):
        self.fiftyfifty_button.config(state='disabled', image=self.used_fiftyfifty)
        options_to_eliminate = []
        correct_option = self.get_correct_option()

        if correct_option == "А":
            options_to_eliminate = random.sample([2,3,4], 2)

        elif correct_option == "Б":
            options_to_eliminate = random.sample([1,3,4], 2)

        elif correct_option == "В":
            options_to_eliminate = random.sample([1,2,4], 2)

        else:
            options_to_eliminate = random.sample([1,2,3], 2)
        
        if 1 in options_to_eliminate:
            self.first_button.config(state='disabled', text="")
        if 2 in options_to_eliminate:
            self.second_button.config( state='disabled', text="")
        if 3 in options_to_eliminate:
            self.third_button.config(state='disabled', text="")
        if 4 in options_to_eliminate:
            self.fourth_button.config(state='disabled', text="")

    def use_call_a_friend(self):
        self.callafriend_button.config(state='disabled', image=self.used_callafriend)
        def get_response():
            user_question = question_entry.get()
            try:
                response = self.chat_with_gpt(user_question)
                response_text.config(state='normal')
                response_text.insert("1.0", "")
                response_text.insert("1.0", response)
                response_text.config(state='disabled')

            except openai.error.RateLimitError:
                response_text.config(state='normal')
                response_text.insert("1.0", "")
                response_text.insert("1.0", "API rate limit exceeded. Please try again later.")
                response_text.config(state='disabled')

        self.input_window = Toplevel(self.root)
        self.input_window.title("Помощ от приятел")
        self.input_window.geometry('700x350+500+235')
        self.input_window.config(bg='white')
        self.input_window.overrideredirect(True)
        
        label = Label(self.input_window, text = "Помощ от приятел", font=(None, 16), width=35, height=3, bg='white', bd=0, fg='black')
        label.pack()

        question_entry = Entry(self.input_window, width=50)
        question_entry.pack(pady=10)

        submit_button = Button(self.input_window, text="Попитай", command=get_response)
        submit_button.pack(pady=10)

        response_text = Text(self.input_window, font=(None,12), width=35, height=15, bd=0, wrap="word", state="disabled", fg="black")
        response_text.pack()

        self.input_window.mainloop()

    def reset_timer(self):
        if hasattr(self.root, 'timer_id'):
            self.root.after_cancel(self.root.timer_id)
        self.timer_seconds = self.TIMER_DURATION
        self.update_timer()

    def show_timeout_popup(self):
        choice = messagebox.askquestion("Time's Up!", "Do you want to start a new game?", icon='warning')
        if choice == 'yes':
            self.try_again()
        else:
            self.back_to_profile()    

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_seconds} seconds")
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            self.root.timer_id = self.root.after(1000, self.update_timer)
        else:
            current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            basicqueries.add_played_game(self.username, "become_rich", current_date, self.questions_answered, "none")
            self.show_timeout_popup()

    def stop_timer(self):
        if hasattr(self.root, 'timer_id'):
            self.root.after_cancel(self.root.timer_id)

    def get_new_question(self):
        if self.questions_answered < 5:
            new_question = self.easy_questions[self.questions_answered]
        elif self.questions_answered >= 5 and self.questions_answered < 10:
            new_question = self.medium_questions[self.questions_answered-5]
        else:
            new_question = self.hard_questions[self.questions_answered-10]
        self.create_questions_frame(self.game_frame, new_question)

    def change_money_picture(self):
        match self.questions_answered:
            case 0:
                image = self.first_sum
            case 1:
                image = self.second_sum
            case 2:
                image = self.third_sum
            case 3:
                image = self.fourth_sum
            case 4:
                image = self.fifth_sum
            case 5:
                image = self.sixth_sum
            case 6:
                image = self.seventh_sum
            case 7:
                image = self.eight_sum
            case 8:
                image = self.ninght_sum
            case 9:
                image = self.tenth_sum
            case 10:
                image = self.eleventh_sum
            case 11:
                image = self.twelfth_sum
            case 12:
                image = self.thirteenth_sum
            case 13:
                image = self.fourteenth_sum
            case 14:
                image = self.fifteenth_sum
        self.create_money_frame(self.root, image)

    def try_again(self):
        self.public_button.config(state='normal', image=self.unused_public)
        self.fiftyfifty_button.config(state='normal', image=self.unused_fiftyfifty)
        self.callafriend_button.config(state='normal', image=self.unused_callafriend)
        self.questions_answered = 0
        random.shuffle(self.easy_questions)
        random.shuffle(self.medium_questions)
        random.shuffle(self.hard_questions)
        self.reset_timer()
        new_question_package = self.easy_questions[len(self.easy_questions)-1]
        self.create_questions_frame(self.game_frame, new_question_package)
        self.create_money_frame(self.root, self.first_sum)
        if self.new_root:
            self.new_root.destroy()

    def back_to_profile(self):
        self.root.destroy()
        profilepage.ProfilePage(self.username)

    def game_over(self):
        self.stop_timer()
        self.new_root = Toplevel()
        self.new_root.config(bg=self.WRONG_ANSWER_COLOUR)
        self.new_root.geometry('375x325+600+350')
        self.new_root.title("Game over")
        self.new_root.overrideredirect(True)
        losing_message = Label(self.new_root, image=self.losing_picture, bd=0)
        losing_message.pack()

        try_again_button = Button(self.new_root, text="Нова игра", font=(None,16,'bold'), bg=self.WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=self.WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=self.try_again)
        try_again_button.pack()
        back_to_profile_button = Button(self.new_root, text="Към профила ми", font=(None,16,'bold'), bg=self.WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=self.WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=self.back_to_profile)
        back_to_profile_button.pack()

    def win_game(self):

        self.stop_timer()
        self.new_root = Toplevel()
        self.new_root.config(bg=self.WRONG_ANSWER_COLOUR)
        self.new_root.geometry('525x625+600+235')
        self.new_root.title("Game won")
        losing_message = Label(self.new_root, image=self.winning_picture, bd=0)
        losing_message.pack()

        try_again_button = Button(self.new_root, text="Нова игра", font=(None,16,'bold'), bg=self.WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=self.WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=self.try_again)
        try_again_button.pack()
        back_to_profile_button = Button(self.new_root, text="Към профила ми", font=(None,16,'bold'), bg=self.WRONG_ANSWER_COLOUR, fg='white', bd=0, activebackground=self.WRONG_ANSWER_COLOUR, activeforeground='white', cursor='hand1', command=self.back_to_profile)
        back_to_profile_button.pack()

    def save_progress(self):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        basicqueries.add_played_game(self.username, "become_rich", current_date, self.questions_answered, "none")

    def mark_answer(self, event):
        self.remove_public_answers()
        
        if self.input_window != None:
            self.input_window.destroy()
        button_marked = event.widget
        if button_marked['state'] != 'disabled':
            button_answer = button_marked['text']
            correct_answer = basicqueries.get_correct_answer(self.current_question)[0][0]
            if button_answer == correct_answer:
                print("Correct!")
                self.questions_answered += 1
                if self.questions_answered < 15:
                    self.reset_timer()
                    self.change_money_picture()
                    self.get_new_question()
                else:
                    self.save_progress()
                    self.win_game()
            else:
                print("Incorrect!")
                self.save_progress()
                self.game_over()
        else:
            pass


if __name__ == '__main__':
    GetRichGame("nzz")
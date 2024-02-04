from tkinter import *

root = Tk()
root.geometry('1520x980')
root.title("Who wants to be a millionaire")

MAIN_COLOUR = '#160559'

root.config(bg=MAIN_COLOUR)

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

game_frame = Frame(root, bg=MAIN_COLOUR, padx=120)
game_frame.grid(row=0, column=0)

hints_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
hints_frame.grid(row=0, column=0)

public_button = Button(hints_frame, image=unused_public, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65)
public_button.grid(row=0, column=0, padx=10)
fiftyfifty_button = Button(hints_frame, image=unused_fiftyfifty, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65)
fiftyfifty_button.grid(row=0, column=1, padx=10)
callafriend_button = Button(hints_frame, image=unused_callafriend, bg=MAIN_COLOUR, bd=0.5, activebackground=MAIN_COLOUR, width=110, height=65)
callafriend_button.grid(row=0, column=2, padx=10)

logo_frame = Frame(game_frame, bg=MAIN_COLOUR)
logo_frame.grid(row=1, column=0)
logo_frame_label = Label(logo_frame, image=logo_picture, bg=MAIN_COLOUR, width = 950, height=450)
logo_frame_label.grid(row=0, column=0)
questions_frame = Frame(game_frame, bg=MAIN_COLOUR, pady=35)
questions_frame.grid(row=2, column=0)
questions_frame_label = Label(questions_frame, image=question_picture, bg=MAIN_COLOUR, width = 950, height=300)
questions_frame_label.grid(row=0, column=0)

money_frame = Frame(root, bg=MAIN_COLOUR, padx=55, pady=45)
money_frame.grid(row=0, column=1)
money_frame_label = Label(money_frame, image=first_sum, bg=MAIN_COLOUR, width=250, height=750)
money_frame_label.grid(row=0, column=0)

root.mainloop()
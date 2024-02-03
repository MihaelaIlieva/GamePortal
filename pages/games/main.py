from tkinter import *



root = Tk()
root.geometry('1520x980')
root.title("Who wants to be a millionaire")

root.config(bg='black')

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

game_frame = Frame(root, bg='black')
game_frame.grid(row=0, column=0)

hints_frame = Frame(game_frame, bg='black')
hints_frame.grid(row=0, column=0)

public_button = Button(hints_frame, image=unused_public, bg='black', bd=1.5, activebackground='black')
public_button.grid(row=0, column=0)
fiftyfifty_button = Button(hints_frame, image=unused_fiftyfifty, bg='black', bd=1.5, activebackground='black')
fiftyfifty_button.grid(row=0, column=1)
callafriend_button = Button(hints_frame, image=unused_callafriend, bg='black', bd=1.5, activebackground='black')
callafriend_button.grid(row=0, column=2)

logo_frame = Frame(game_frame, bg='black')
logo_frame.grid(row=1, column=0)
logo_frame_label = Label(logo_frame, image=logo_picture, bg='black')
logo_frame_label.grid(row=0, column=0)
questions_frame = Frame(game_frame, bg='black')
questions_frame.grid(row=2, column=0)

money_frame = Frame(root, bg='black')
money_frame.grid(row=0, column=1)
money_frame_label = Label(money_frame, image=first_sum, bg='black')
money_frame_label.grid(row=0, column=0)

root.mainloop()
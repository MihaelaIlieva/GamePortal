import profilepage
import database.basicqueries as basicqueries
from tkinter import Tk, Label, PhotoImage, Button, Entry

class LoginPage:

    def __init__(self):
        self.root = Tk()
        self.root.title("Game Portal - Login Page")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.MAIN_COLOUR = '#100235'
        self.FONT_COLOUR = '#8c198f'
        self.FONT_COLOUR = '#ffffff'
        
        self.error_message = None    

        self.background_label = Label(self.root)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_image = PhotoImage(file="images/pagebackground.png")
        self.background_label.configure(image=self.background_image)
        
        self.text_label = Label(self.root, text="Please put in your credentials", font=(None, 20), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.text_label.place(relx=0.5, rely=0.10, anchor="center")

        self.picture_label = Label(self.root, bg=self.MAIN_COLOUR)
        self.picture_label.place(relx=0.5, rely=0.25, anchor="center")
        self.picture_image = PhotoImage(file="images/background_old.png")
        self.picture_label.configure(image=self.picture_image)

        self.username_label = Label(self.root, text="Username", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.username_label.place(relx=0.5, rely=0.37, anchor="center")

        self.password_label = Label(self.root, text="Password", font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.password_label.place(relx=0.5, rely=0.47, anchor="center")

        self.username_entry = Entry(self.root, font=(None, 14))
        self.username_entry.place(relx=0.5, rely=0.41, anchor="center")

        self.password_entry = Entry(self.root, font=(None, 14), show="*")
        self.password_entry.place(relx=0.5, rely=0.51, anchor="center")

        self.login_button = Button(self.root, text="Login", font=(None, 14), bg="#ffcced", activebackground="#fe67c2", command=self.login, width=10)
        self.login_button.place(relx=0.5, rely=0.57, anchor="center")

        self.error_message_label = Label(self.root, text=self.error_message, font=(None, 14), bd=0, bg=self.MAIN_COLOUR, fg=self.FONT_COLOUR)
        self.error_message_label.place(relx=0.5, rely=0.61, anchor="center")
        
        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(basicqueries.check_for_same_username(username)) == 0:
            self.error_message = "No such user!"
            self.error_message_label.config(text=self.error_message)
            print("No such user!")

        else:
            user_id = basicqueries.check_for_same_username(username)[0][0]
            result = basicqueries.get_user_credentials(user_id)

            if result[0] == (username, password):
                self.error_message = "Successful login!"
                self.error_message_label.config(text=self.error_message)
                print("Successful login!")
                self.root.after(500, lambda: self.redirect_to_profilepage(username, password))

            else:
                self.error_message = "Wrong password!"
                self.error_message_label.config(text=self.error_message)
                print("Wrong password!")

    def redirect_to_profilepage(self, username, password):
        self.root.destroy()
        profilepage.ProfilePage(username, password)

if __name__ == "__main__":
    app = LoginPage()


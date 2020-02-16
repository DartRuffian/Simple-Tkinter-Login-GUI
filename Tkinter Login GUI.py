from tkinter import *; from os import listdir

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack() # .pack() organizes widgets in blocks before placing them in the parent widget.
        self.main_account_screen() # creates a main screen with a login and register button
    
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        
    def main_account_screen(self):
        Label(self, text = "Select either Register or Login", bg = "dim gray", width = "300", height = "2", font = ("Calibri", 15)).pack()
        for i in range(3):
            Label(self, text = "").pack()
        Button(self, text = "Register", height = "2", width = "30", command = self.register).pack()
        Label(self, text = "").pack()
        Button(self, text = "Login", height = "2", width = "30", command = self.login).pack()
        
    def register(self):
        self.register_screen = Toplevel(main_screen)
        self.register_screen.title("Register Window")
        setup_screen(self.register_screen, 400, 250)
        self.username = StringVar(); self.password = StringVar()
        Label(self.register_screen, text = "Please enter your details below.", bg = "dim gray", width = "300", height = "2", font = ("Calibri", 12)).pack()
        Label(self.register_screen, text = "Username").pack()
        usernameEntry = Entry(self.register_screen, textvariable = self.username); usernameEntry.pack()
        Label(self.register_screen, text = "Password").pack()
        passwordEntry = Entry(self.register_screen, textvariable = self.password, show = "*"); passwordEntry.pack() # show has all the text show up as the value
        Label(self.register_screen, text = "").pack()
        Button(self.register_screen, text = "Register", width = 10, height = 1, command = self.register_user).pack()
    
    def register_user(self):
        usernameInfo = self.username.get()
        passwordInfo = self.password.get()
        with open(usernameInfo, "w") as f:
            f.write(usernameInfo + "\n")
            f.write(passwordInfo)
        Label(self.register_screen, text = "Registration Complete", fg = "green").pack()
        Label(self.register_screen, text = "You may now close this window.").pack()
        
    def login(self):
        self.login_screen = Toplevel(main_screen)
        setup_screen(self.login_screen, 400, 250)
        Label(self.login_screen, text = "Please enter your login credentials.", bg = "dim gray", width = "300", height = "2", font = ("Calibri", 12)).pack()
        self.usernameVerify = StringVar(); self.passwordVerify = StringVar()
        
        Label(self.login_screen, text = "Username").pack()
        usernameEntry = Entry(self.login_screen, textvariable = self.usernameVerify); usernameEntry.pack()
        
        Label(self.login_screen, text = "Password").pack()
        passwordEntry = Entry(self.login_screen, textvariable = self.passwordVerify, show = "*"); passwordEntry.pack()
        Label(self.login_screen, text = "").pack()
        Button(self.login_screen, text = "Login", width = 10, height = 1, command = self.login_verification).pack()
        
    def login_verification(self):
        username_ = self.usernameVerify.get(); password_ = self.passwordVerify.get()
        
        listOfFiles = os.listdir()
        if username_ in listOfFiles:
            with open(username_, "r") as f:
                verify = f.read().splitlines()
                if password_ in verify:
                    self.login_success()
                else:
                    self.invalid_password()
        else:
            self.user_not_found()
            
    def login_success(self):
        popup_screen = Toplevel(main_screen)
        popup_screen.title("Success!")
        setup_screen(popup_screen, 150, 100)
        
        Label(popup_screen, text = "Login was successful.").pack()
        self.clear_window()
        Button(popup_screen, text = "Ok", command = popup_screen.destroy).pack()
        Label(self.login_screen, text = "Successful Login", fg = "green").pack()
        Label(self.login_sceen, text = "Very important data here.").pack()
        
    def invalid_password(self):
        popup_screen = Toplevel(main_screen)
        popup_screen.title("Invalid password")
        setup_screen(popup_screen, 150, 100)
        
        Label(popup_screen, text = "The entered password is invalid.").pack()
        Button(popup_screen, text = "Ok", command = popup_screen.destroy).pack()
        
    def user_not_found(self):
        popup_screen = Toplevel(main_screen)
        popup_screen.title("User not found")
        setup_screen(popup_screen, 150, 100)
        
        Label(popup_screen, text = "User was not found.").pack()
        Button(popup_screen, text = "Ok", command = popup_screen.destroy).pack()
    
def setup_screen(screen_title, w, h):
    global x; global y
    ws = screen_title.winfo_screenwidth()
    hs = screen_title.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    screen_title.geometry('%dx%d+%d+%d' % (w, h, x, y))

main_screen = Tk()
main_screen.title("Custom Application - Simple Login Gui")
setup_screen(main_screen, 450, 450)
app = Application(main_screen)
main_screen.mainloop()

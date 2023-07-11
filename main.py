from tkinter import *

from pages.login import LoginPage


class MainApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x550+290+40")
        self.root.title("Authenticator App")
        self.runLogin()
        self.root.mainloop()


    def runLogin(self):
        return LoginPage(self.root)


print(MainApp())
from tkinter import *
from tkinter import  messagebox as mb
from backend.class_file import Authenticator
from pages.register import RegisterPage
from backend.instanciation import objet1
Font1 = ('Arial',20,'bold')
Font2 = ('Arial',15,'bold')
Font3 = ('Arial',14,'bold')

class LoginPage:
    def __init__(self, root):
        self.root = root
        frame = Canvas(root, width=800, height=550)
        Label(frame,text="CONNEXION",font=Font1).place(x=323,y=45)

        # nom d'utilisateur ....
        Label(frame,text='Username : ',font=Font2).place(x=200,y=150)
        self.username = Entry(frame,font=Font2)
        self.username.place(x=330,y=150)

        # Mot de passe ...
        Label(frame, text='Password : ', font=Font2).place(x=200, y=210)
        self.password = Entry(frame, font=Font2,show="*")
        self.password.place(x=330, y=210)

        # Boutons de connexion et de creation de compte ...
        from pages.home import HomePage

        Button(frame,text="     Register     ",font=Font3,bg='orange',fg='white',
               command=lambda : RegisterPage(root)).place(x=230,y=300)
        Button(frame,text="     Connexion     ",font=Font3,bg='blue',fg='white',
               command=self.connexion).place(x=420,y=300)

        frame.place(x=0,y=0)

    def connexion(self):
        from pages.home import HomePage
        objet1.login(self.username.get(), self.password.get())
        HomePage(self.root, self.username.get())


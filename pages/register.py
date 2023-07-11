from tkinter import *
from tkinter import  messagebox as mb
from backend.class_file import Authenticator
from backend.instanciation import objet1

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',15,'bold')
Font3 = ('Arial',14,'bold')

class RegisterPage:
    def __init__(self, root):
        self.root = root
        frame = Canvas(root, width=800, height=550)
        Label(frame,text="REGISTER",font=Font1).place(x=323,y=45)

        # nom d'utilisateur ....
        Label(frame,text='Username : ',font=Font2).place(x=200,y=150)
        self.username = Entry(frame,font=Font2)
        self.username.place(x=330,y=150)

        # Mot de passe ...
        Label(frame, text='Password : ', font=Font2).place(x=200, y=210)
        self.password = Entry(frame, font=Font2,show="*")
        self.password.place(x=330, y=210)

        # Boutons de connexion et de creation de compte ...
        from pages.login import LoginPage
        from pages.home import HomePage

        Button(frame,text="      Login      ",font=Font3,bg='orange',fg='white',
               command=lambda : LoginPage(root)).place(x=230,y=300)
        Button(frame,text="     Register     ",font=Font3,bg='blue',fg='white',
               command=self.register).place(x=420,y=300)

        frame.place(x=0,y=0)
    def register(self):
        from pages.home import HomePage

        try:
            objet1.add_user(self.username.get(), self.password.get())
            mb.showinfo('Information', "Account created succesfully !")
            return HomePage(self.root, self.username.get())
        except:
            mb.showerror('Error',"utilisateur exiatant/ mot de passe court !")

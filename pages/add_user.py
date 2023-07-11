from tkinter import *
from tkinter import messagebox as mb
from backend.instanciation import  objet1

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',17,'italic')
Font3 = ('Arial',15,'bold')

class AddUser:
    def __init__(self, root):
        frame = Canvas(root, width=600, height=500,bg='lightblue')
        Label(frame,text="Add a new user",font=Font2,bg='lightblue').place(x=250,y=20)

        #  champs pour ajouter un user ...
        Label(frame,text='Username :',font=Font2,bg='lightblue').place(x=70,y=100)
        self.username = Entry(frame,font=Font2)
        self.username.place(x=210,y=100)

        Label(frame, text='Password :', font=Font2, bg='lightblue').place(x=70, y=170)
        self.password = Entry(frame, font=Font2)
        self.password.place(x=210, y=170)

        Button(frame, text='   Clear   ', bg='purple',font=Font2,fg='white',command=self.clear_fields).place(x=130,y=290)
        Button(frame, text='   Add user   ', bg='teal', font=Font2,fg='white',command=self.add_user).place(x=340, y=290)
        frame.place(x=0,y=0)

    def clear_fields(self):
        # Effacer les valeurs des champs ...

        self.username.delete(0,END)
        self.password.delete(0, END)
    def add_user(self):
        try:
            objet1.add_user(self.username.get(), self.password.get())
            mb.showinfo("Information", "Utilisateur ajoute avec succes !")
            self.clear_fields()
        except:
            mb.showinfo("Erreur", "Donnees invalides !")

        # mb.showinfo("Information", "Utilisateur ajoute !")
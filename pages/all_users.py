from tkinter import *
from tkinter import ttk
from backend.instanciation import objet1

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',17,'italic')
Font3 = ('Arial',15,'bold')

class AllUsers:
    def __init__(self, root):
        frame = Canvas(root, width=600, height=500,bg='lightblue')
        Label(frame,text="List of users",font=Font2,bg='lightblue').place(x=250,y=20)

        # data users
        data_user = objet1.users

        # tableau des utilisateurs.
        table = ttk.Treeview(frame,columns=('username', 'password'),show='headings')
        table.heading('username',text='Username')
        table.heading('password', text='Password')
        table.place(x=100, y=90)
        for i in range(len(data_user)):
            data = (list(data_user.keys())[i], data_user[list(data_user.keys())[i]].password )
            print(data)
            table.insert(parent='',index=0,values=data)


        frame.place(x=0,y=0)
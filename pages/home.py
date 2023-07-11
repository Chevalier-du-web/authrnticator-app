from tkinter import *
from pages.register import RegisterPage
from pages.all_users import AllUsers
from pages.add_user import AddUser
from pages.delete_user import DeleteUser
from pages.add_permission import AddPermission
from pages.delete_permission import DeletePermission

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',16,'italic')
Font3 = ('Arial',15,'bold')
texte = 'Gerez vos utilisateurs de maniere \nplus professionnelle et securisee !'

class HomePage:
    def __init__(self, root,username):
        frame = Canvas(root, width=800, height=550)
        frame2 = Canvas(root, width=800, height=50,bg='orange')
        Label(frame2,text="AUTHENTICATOR APP -- HOME             "
                          f"                     Welcome {username}",font=Font2,bg='orange').place(x=23,y=10)
        frame2.place(x=0, y=0)

        # menu de l'application
        from pages.login import LoginPage
        frame3 = Canvas(root, width=200, height=500,bg='grey')
        #  liste des menus ...
        Button(frame3,text="   Users   ",font=Font2,command= lambda  : AllUsers(frame4)).place(x=8,y=20,width=190)
        Button(frame3, text="   Add user   ", font=Font2,command= lambda  : AddUser(frame4)).place(x=8, y=75, width=190)
        Button(frame3, text="   Delete user   ", font=Font2,command= lambda  : DeleteUser(frame4)).place(x=8, y=130, width=190)
        Button(frame3, text="   Add permission   ", font=Font2,command= lambda  : AddPermission(frame4)).place(x=8, y=185, width=190)
        Button(frame3, text="   Delete permission   ", font=Font2,command= lambda  : DeletePermission(frame4)).place(x=8, y=240, width=190)
        Button(frame3, text="   Logout   ", font=Font2,command=lambda  : LoginPage(root)).place(x=8, y=295, width=190)
        Button(frame3, text="   Exit   ", font=Font2,command=root.destroy).place(x=8, y=350, width=190)

        frame3.place(x=0, y=50)

        # contenu de la page ...
        frame4 = frame3 = Canvas(root, width=600, height=500,bg='lightblue')
        Label(frame4,text=texte,font=Font1,bg='lightblue').\
        place(x=85,y=150)

        frame4.place(x=200, y=50)

        frame.place(x=0,y=0)

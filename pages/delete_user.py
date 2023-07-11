from tkinter import *

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',17,'italic')
Font3 = ('Arial',15,'bold')

class DeleteUser:
    def __init__(self, root):
        frame = Canvas(root, width=600, height=500,bg='lightblue')
        Label(frame,text="Delete a user",font=Font2,bg='lightblue').place(x=250,y=20)
        #  champs pour ajouter un user ...
        Label(frame, text='Username :', font=Font2, bg='lightblue').place(x=70, y=150)
        self.username = Entry(frame, font=Font2)
        self.username.place(x=210, y=150)


        Button(frame, text='   Clear   ', bg='purple', font=Font2, fg='white', command=self.clear_fields).place(x=130, y=290)
        Button(frame, text='   Delete user   ', bg='teal', font=Font2, fg='white', command=self.delete_user).place(x=340, y=290)
        frame.place(x=0, y=0)

        frame.place(x=0,y=0)

    def clear_fields(self):
        # Effacer les valeurs des champs ...
        self.username.delete(0,END)

    def delete_user(self):
        from backend.instanciation import objet1
        objet1.delete_user(self.username.get())
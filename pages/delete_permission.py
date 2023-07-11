from tkinter import *

Font1 = ('Arial',20,'bold')
Font2 = ('Arial',17,'italic')
Font3 = ('Arial',15,'bold')

class DeletePermission:
    def __init__(self, root):
        frame = Canvas(root, width=600, height=500,bg='lightblue')
        Label(frame,text="Delete permission from a user",font=Font2,bg='lightblue').place(x=250,y=20)

        #  champs pour ajouter une permission  ...
        Label(frame, text='Username :', font=Font2, bg='lightblue').place(x=70, y=100)
        self.username = Entry(frame, font=Font2)
        self.username.place(x=210, y=100)

        Label(frame, text='Permission :', font=Font2, bg='lightblue').place(x=70, y=170)
        self.permission = Entry(frame, font=Font2)
        self.permission.place(x=210, y=170)

        Button(frame, text='   Clear   ', bg='purple', font=Font2, fg='white', command=self.clear_fields).place(x=130,
                                                                                                                y=290)
        Button(frame, text='   Delete permission   ', bg='teal', font=Font2, fg='white',
               command=self.delete_permission).place(
            x=300, y=290)
        frame.place(x=0,y=0)

    def clear_fields(self):
        # Effacer les valeurs des champs ...
        self.username.delete(0, END)
        self.permission.delete(0, END)

    def delete_permission(self):
        from backend.instanciation import perms
        perms.delete_permission(self.permission.get(),self.username.get())
        self.clear_fields()
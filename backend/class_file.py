# TP3 : Systeme d'authentification et d'autorisation des utilisateurs
#  Sangon Brandon : 23583
from tkinter import  messagebox as mb

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        # Partie de chiffrement du mot de passe du user
        import hashlib as hl
        return hl.md5(password.encode()).hexdigest()

    def authenticate(self, password):
        # verifier le mot de passe du user ...
        return self.password == self._encrypt_password(password)


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise mb.showerror("Error", "User existant!")
        self.users[username] = User(username, password)
    def delete_user(self, username):
        if username in self.users:
            self.users.pop(username)
            mb.showinfo("Information","User deleted !")
        else:
            mb.showerror("Error","User not found !")


    def login(self, username, password):
        if username not in self.users:
            print(list(self.users.keys()),username)
            raise mb.showerror("Error !","User not found")
        user = self.users[username]
        if not user.authenticate(password):
            # AuthException("Mot de passe incorrect !", username, user)
            raise mb.showerror('Error',"invalid password !")
        mb.showinfo('Information',"User conncted !")

    def logout(self, username):
        # Déconnexion de l'utilisateur
        print("User disconnected")


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    # ajouter une permission a un user
    def add_permission(self, permission,username):
        if permission not in self.permissions:
            self.permissions[permission] = set()
            mb.showinfo("Information", "permission added")

    def delete_permission(self, permission,username):
        if permission in self.permissions:
            self.permissions.pop(permission)
            mb.showinfo("Information", "permission deleted")
        else:
            mb.showerror("Information", "permission not founded")

    # verifier la permission
    def verifier_permission(self, username, permission):
        if username not in self.authenticator.users:
            raise AuthException("utilisateur non existant", username)
        user = self.authenticator.users[username]
        if permission not in self.permissions:
            raise AuthException("Permission introuvable", username, user)
        if user not in self.permissions[permission]:
            raise AuthException("utilisateur non non permi", username, user)
        print("l\'utilisateur es permi ")

# instanciation de la classe Authenticator ...
objet1 = Authenticator()


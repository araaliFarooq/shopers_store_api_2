# controller class for user
from app.db.db_functions import DBFunctions
from app.models.user import User


class UserController:
    def __init__(self):
        self.dbcon = DBFunctions()

    def add_attendant(self, user_name, contact, role, password):
        # add new attendant
        user = User(user_name, contact, role, password)
        self.dbcon.add_new_user(
            user_name=user.user_name, contact=user.contact, role=user.role, password=user.password)
        return True
    
    def check_if_user_exists(self, user_name):
        # check if the supplied username already exists.
        user_exists = self.dbcon.is_username_exist(user_name=user_name)
        if user_exists:
            return user_exists
        return False

    def check_if_contact_exists(self, contact):
        # check if the supplied contact already exists.
        contact_exists = self.dbcon.is_contact_exist(contact=contact)
        if contact_exists:
            return True
        return False

    def user_login(self, user_name, password):
        # user login
        login = self.dbcon.user_login(user_name=user_name, password=password)
        if login:
            return login
        return False

    def get_user_role(self, user_name):
        # get current user's role
        user = self.dbcon.is_username_exist(user_name=user_name)
        return user

    def update_user_role(self, user_name, role):
        # update current user's role
        user_update= self.dbcon.update_user(username=user_name, role=role)
        return user_update  

    def get_all_users(self):
        # get all registered users.
        users = self.dbcon.get_all_attendants()
        return users
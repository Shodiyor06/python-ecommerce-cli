import email
from typing import List

from models.user import User

# from utils.utils import make_password
from utils.validators import validate_name

from services.database import DB


class UserService:
    
    def __init__(self):
        self.logged_user = None
        self.db = DB()
        self.users: List[User] = []
    
    def create_user(self):
        username = input("Foydalanuvchi nomini kiriting: ").strip().lower()
        first_name = input("Ismingizni kiriting: ").strip().capitalize()
        last_name = input("Familiyangizni kirting: ").strip().capitalize()
        password = input("Parol kiriting: ")

        if not validate_name(first_name):
            print("First Name xato kiritgansiz.")
            return
        elif not validate_name(last_name):
            print("Last Name xato kiritgansiz.")
            return

        user = User.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        self.db.create_user(user.to_dict())
        print("Siz muvaffaqiyatli royxatdan otdingiz.")

    def login_user(self):
        username = input("Foydalanuvchi nomini kiriting: ").strip().lower()
        password = input("Parol kiriting: ")

        if not validate_name(username):
            print("Username xato kiritgansiz.")
        user_data = self.db.get_users(username, password)

        if user_data:
            self.logged_user = User.create_user(
                username=user_data['username'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name']
            )
            self.logged_user.id = user_data['id']
            print("Siz muvaffaqiyatli kirdingiz.")
        else:
            print("Bunda user mavjud emas.")

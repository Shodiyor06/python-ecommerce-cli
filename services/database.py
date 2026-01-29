import json


class DB:
    def __init__(self, db_file="db.json"):
        self.db_file = db_file
        self.data = {"users": [], "products": [], "orders": []}
        self.load_data_user()
        self.load_data_product()

    def load_data_user(self):
        with open(self.db_file, "r") as f:
            self.data = json.loads(f.read())

    def load_data_product(self):
        with open(self.db_file, "r") as f:
            self.data = json.loads(f.read())

    def save_data(self):
        with open(self.db_file, "w") as f:
            f.write(json.dumps(self.data, indent=4))

    def create_user(self, user):
        self.data["users"].append(user)
        self.save_data()
        print("ro'yxatdan o'tdingiz.")

    def create_product(self, product):
        self.data["products"].append(product)
        self.save_data()

    def get_users(self, username: str, password: str):
        for user_data in self.data["users"]:
            if user_data["username"] == username and user_data["password"] == password:
                return user_data

    def get_products(self):
        return self.data["products"]

class User:
    def __init__(self, id, username, password, first_name, last_name):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name
        }   
    @classmethod
    def create_user(cls, first_name, last_name, username, password):
        return cls(
            id=None,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
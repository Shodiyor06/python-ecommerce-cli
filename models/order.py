class Order:
    def __init__(self, id, username, total_price):

        self.id = id
        self.username = username
        self.total_price = total_price
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "total_price": self.total_price,
        }   
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            total_price=data.get('total_price'),
        )
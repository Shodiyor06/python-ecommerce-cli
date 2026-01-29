import json
from models.order import Order
from models.user import User
from models.product import Product

class OrderService:
    def __init__(self):
        self.file_path = "data/db.json"
        self.orders = self.load_orders()

    def load_orders(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                orders = []
                for item in data.get("orders", []):
                    user = User(name=item["user"]["name"])
                    products = [Product(p["name"], p["price"]) for p in item["products"]]
                    orders.append(Order(user, products))
                return orders
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_orders(self):
        data = {
            "orders": [
                {
                    "user": {"name": order.user.name},
                    "products": [{"name": p.name, "price": p.price} for p in order.products]
                }
                for order in self.orders
            ]
        }
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def create_order(self, user: User, products: list[Product]) -> None:
        order = Order(user=user, products=products)
        self.orders.append(order)
        self.save_orders()
        print("Buyurtma muvaffaqiyatli yaratildi.")

    def get_orders(self) -> list:
        return self.orders

    def print_check(self):
        if not self.orders:
            print("Hozircha hech qanday buyurtma mavjud emas.")
            return

        order = self.orders[-1]
        print("\n=== CHEK ===")
        print(f"Foydalanuvchi: {order.user.name}")
        print("Mahsulotlar:")
        total = 0
        for product in order.products:
            print(f"- {product.name}: {product.price} so'm")
            total += product.price
        print(f"Jami: {total} so'm\n")

    def delete_order(self, order_index: int) -> None:
        if 0 <= order_index < len(self.orders):
            deleted_order = self.orders.pop(order_index)
            self.save_orders()
            print(f"Buyurtma o'chirildi")
        else:
            print("Noto'g'ri buyurtma indeksi.")
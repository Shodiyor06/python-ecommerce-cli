import json
from models.order import Order
from models.user import User
from models.product import Product

class OrderService:
    def __init__(self):
        self.file_path = "db.json"
        self.orders = self.load_orders()

    def load_orders(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            orders = []
            for item in data.get("orders", []):
                # User yaratish - to'g'ri parametrlar
                user = User(
                    id=item["user"]["id"],
                    username=item["user"]["username"],
                    password=item["user"]["password"],
                    first_name=item["user"]["first_name"],
                    last_name=item["user"]["last_name"]
                )
                
                # Products yaratish - to'g'ri parametrlar
                products = [
                    Product(
                        id=p["id"],
                        name=p["name"],
                        category=p["category"],
                        price=p["price"],
                        sale=p["sale"],
                        stock=p["stock"],
                        description=p["description"]
                    ) 
                    for p in item["products"]
                ]
                
                # Order yaratish
                order = Order(
                    id=item["id"],
                    user=user,
                    products=products,
                    total_price=item["total_price"]
                )
                orders.append(order)
                
                return orders
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_orders(self):
        """Buyurtmalarni db.json faylga saqlash"""
        data = None
        
        try:
            # Avvalgi ma'lumotlarni o'qish (users va products ni saqlab qolish)
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Fayl topilmadi: {self.file_path}")
            data = None
        except json.JSONDecodeError:
            print(f"JSON parse xatosi")
            data = None
        
        # ✅ Agar data None bo'lsa, yangi struktura yaratish
        if data is None:
            data = {"users": [], "products": [], "orders": []}
        
        # ✅ Order modeliga mos qilib saqlash
        if isinstance(self.orders, list):
            data["orders"] = [
                {
                    "id": order.id,
                    "username": order.username,
                    "total_price": order.total_price,
                    "products": getattr(order, 'products', [])  # Agar products bo'lsa saqlash
                }
                for order in self.orders
            ]
        else:
            data["orders"] = []
        
        # ✅ Faylga yozish
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Fayl saqlanishda xato: {e}")

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
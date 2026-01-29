import json
from models.order import Order
from models.user import User
from models.product import Product


class OrderService:
    def __init__(self):
        self.file_path = "db.json"
        self.orders = []
        self.cart = {}  # {username: [products]}
        self.load_orders()

    def load_orders(self):
        """Buyurtmalarni fayldan yuklash"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # ✅ Barcha buyurtmalarni yuklash (return qilmasdan)
            for item in data.get("orders", []):
                try:
                    order = Order(
                        id=item.get("id"),
                        username=item.get("username"),
                        total_price=item.get("total_price", 0)
                    )
                    order.products = item.get("products", [])
                    self.orders.append(order)
                except Exception as e:
                    print(f"Buyurtma yuklashda xato: {e}")
                    
        except FileNotFoundError:
            print(f"Fayl topilmadi: {self.file_path}. Yangi fayl yaratiladi.")
            self.orders = []
        except json.JSONDecodeError:
            print(f"JSON parse xatosi")
            self.orders = []

    def save_orders(self):
        """Buyurtmalarni db.json faylga saqlash"""
        try:
            # Avvalgi users va products ma'lumotlarni saqlab qolish
            existing_data = {}
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    existing_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                existing_data = {"users": [], "products": [], "orders": []}
            
            # ✅ Order modeliga mos qilib saqlash
            existing_data["orders"] = [
                {
                    "id": order.id,
                    "username": order.username,
                    "total_price": order.total_price,
                    "products": getattr(order, 'products', [])
                }
                for order in self.orders
            ]
            
            # Faylga yozish
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)
                
        except Exception as e:
            print(f"Fayl saqlanishda xato: {e}")

    def create_order(self, user: User, products: list = None) -> None:
        """Yangi buyurtma yaratish"""
        if products is None:
            products = []
        
        # ✅ Jami narxni hisoblash
        total_price = 0
        if products:
            for p in products:
                if isinstance(p, dict):
                    total_price += p.get("product price", 0)
                else:
                    total_price += p.price
        
        # ✅ Order yaratish - Order modeliga mos
        order = Order(
            id=len(self.orders) + 1,
            username=user.username,
            total_price=total_price
        )
        order.products = products
        
        self.orders.append(order)
        self.save_orders()
        print("Buyurtma muvaffaqiyatli yaratildi.")

    def get_orders(self) -> list:
        """Barcha buyurtmalarni olish"""
        return self.orders

    def print_check(self):
        """Oxirgi buyurtmaning chekini chop etish"""
        if not self.orders:
            print("Hozircha hech qanday buyurtma mavjud emas.")
            return

        order = self.orders[-1]
        print("\n" + "="*60)
        print("                         CHEK".center(60))
        print("="*60)
        print(f"Foydalanuvchi: {order.username}")
        print("-"*60)
        print("Mahsulotlar:")
        
        total = 0
        if hasattr(order, 'products') and order.products:
            for i, product in enumerate(order.products, 1):
                if isinstance(product, dict):
                    # Dictionary formatda saqlangan mahsulot
                    name = product.get("product name", "Noma'lum")
                    price = product.get("product price", 0)
                else:
                    # Product obekt
                    name = product.name
                    price = product.price
                
                print(f"{i}. {name}: {price:,} so'm")
                total += price
        
        print("-"*60)
        print(f"Jami narx: {total:,} so'm")
        print("="*60 + "\n")

    def add_to_cart(self, username: str, product: dict):
        """Savatga mahsulot qo'shish"""
        if username not in self.cart:
            self.cart[username] = []
        
        self.cart[username].append(product)
        name = product.get("product name", "Mahsulot")
        print(f"'{name}' savatga qo'shildi.")

    def get_cart(self, username: str) -> list:
        """Foydalanuvchining savatini olish"""
        return self.cart.get(username, [])

    def clear_cart(self, username: str):
        """Savatni tozalash"""
        if username in self.cart:
            self.cart[username] = []
            print("Savat tozalandi.")
        else:
            print("Savat bo'sh yoki topilmadi.")

    def remove_from_cart(self, username: str, product_index: int):
        """Savatdan mahsulot olib tashlash"""
        if username in self.cart and 0 <= product_index < len(self.cart[username]):
            product = self.cart[username].pop(product_index)
            name = product.get("product name", "Mahsulot")
            print(f"'{name}' savatdan olib tashlandi.")
        else:
            print("Noto'g'ri mahsulot indeksi yoki savat bo'sh.")
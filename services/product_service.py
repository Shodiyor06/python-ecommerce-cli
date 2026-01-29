class ProductService:
    """Mahsulotlarni boshqarish"""
    
    def __init__(self, products):
        self.products = products

    def print_products(self):
        """Barcha mahsulotlarni ko'rsatish"""
        if not self.products:
            print("Hech qanday mahsulot topilmadi.")
            return
        
        print("\n" + "="*70)
        print("MAVJUD MAHSULOTLAR".center(70))
        print("="*70)
        
        for i, product in enumerate(self.products, 1):
            name = product.get("product name", "Noma'lum")
            price = product.get("product price", "Narx ko'rsatilmagan")
            stock = product.get("product stock", 0)
            
            print(f"{i}. {name}")
            print(f"   Narx: {price:,} so'm | Omborda: {stock} dona")
        
        print("="*70 + "\n")

    def add_product_to_cart(self, order_service, username, products):
        """Savatga mahsulot qo'shish"""
        self.print_products()
        
        try:
            product_index = int(input("Mahsulot raqamini tanlang: ")) - 1
            
            if 0 <= product_index < len(products):
                product = products[product_index]
                order_service.add_to_cart(username, product)
            else:
                print("Noto'g'ri mahsulot raqami.")
        except ValueError:
            print("Raqam kiriting.")

    def print_cart(self, order_service, username):
        """Savatni ko'rsatish"""
        cart = order_service.get_cart(username)
        
        if not cart:
            print("Savat bo'sh.")
            return
        
        print("\n" + "="*70)
        print("SAVAT".center(70))
        print("="*70)
        
        total = 0
        for i, product in enumerate(cart, 1):
            name = product.get("product name", "Noma'lum")
            price = product.get("product price", 0)
            print(f"{i}. {name}: {price:,} so'm")
            total += price
        
        print("-"*70)
        print(f"Jami: {total:,} so'm")
        print("="*70 + "\n")

    def remove_product_from_cart(self, order_service, username):
        """Savatdan mahsulot olib tashlash"""
        cart = order_service.get_cart(username)
        
        if not cart:
            print("Savat bo'sh.")
            return
        
        print("Savat:")
        for i, product in enumerate(cart, 1):
            name = product.get("product name", "Noma'lum")
            price = product.get("product price", 0)
            print(f"{i}. {name}: {price:,} so'm")
        
        try:
            product_index = int(input("O'chirish uchun raqamni tanlang: ")) - 1
            order_service.remove_from_cart(username, product_index)
        except ValueError:
            print("Raqam kiriting.")
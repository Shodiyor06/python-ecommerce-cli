class Product:
    def __init__(self, id, name, category, price, sale, stock, description):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.sale = sale
        self.stock = stock
        self.description = description

    def to_dict_p(self):
        return {
            "product id": self.id,
            "product name": self.name,
            "product category": self.category,
            "product price": self.price,
            "product sale": self.sale,
            "product stock": self.stock,
            "product description": self.description
        }
    
    @classmethod
    def from_dict_p(cls, data):
        return cls(
            id=data.get('product id'),
            name=data.get('product name'),
            category=data.get('product category'),
            price=data.get('product price'),
            sale=data.get('product sale'),
            stock=data.get('product stock'),
            description=data.get('product description')
        )
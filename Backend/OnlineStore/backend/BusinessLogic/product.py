from ..models import Product
from .category import category


class product(Product):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Product):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @staticmethod
    def all():
        return Product.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return Product.objects.get(args, kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return Product.objects.filter(args, kwargs)

    def addStock(self, quantity):
        self.stock += quantity
        self.save()

    def setStock(self, quantity):
        self.stock = quantity
        self.save()

    def removeStock(self, quantity):
        if self.stock < quantity:
            return False
        self.stock -= quantity
        self.save()
        return True

    def update(self, product_name, product_description, product_stock, product_price, product_discount, product_category: category):
        try:
            self.name = product_name
            self.description = product_description
            self.stock = product_stock
            self.price = product_price
            self.discount = product_discount
            self.category = product_category
            self.save()
        except:
            raise Exception("Couldn't update Product for Shop, [Product Name]:" + str(product_name) +
                            ", [Product Description]:" + str(product_description) + ", [Quantity]:" + str(product_stock))

    def removeProduct(self):
        self.isRemoved = True
        self.save()

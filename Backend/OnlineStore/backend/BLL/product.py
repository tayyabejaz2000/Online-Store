from ..models import ProductModel
from .category import category


class product:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ProductModel):
            self.data = args[0]
        else:
            self.data = ProductModel(*args, **kwargs)

    @staticmethod
    def all():
        return ProductModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        return ProductModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        return ProductModel.objects.filter(*args, **kwargs)

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

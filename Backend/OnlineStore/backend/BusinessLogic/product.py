from ..models import Product


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

    def removeStock(self, quantity):
        self.stock -= quantity
        self.save()

from ..models import OrderModel
from .product import product
from .orderedproduct import orderedproduct


class order:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], OrderModel):
            self.data = args[0]
        else:
            self.data = OrderModel(*args, **kwargs)

    @staticmethod
    def all():
        OrderModel.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        OrderModel.objects.get(*args, **kwargs)

    @staticmethod
    def filter(*args, **kwargs):
        OrderModel.objects.get(*args, **kwargs)

    def addProduct(self, prod: product, quantity):
        try:
            o = orderedproduct(order=self.data,
                               product=prod.data, quantity=quantity)
            if (prod.removeStock(quantity)):
                o.save()
        except:
            raise Exception("Couldn't Add Product to Order")

    def save(self):
        self.data.save()

from ..models import OrderModel
from .product import product
from .orderedproduct import orderedproduct


class order:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], OrderModel):
            self.data = args[0]
        else:
            self.data = OrderModel(*args, **kwargs)

    def addProduct(self, prod: product, quantity):
        try:
            o = orderedproduct(order=self.data,
                               product=prod, quantity=quantity)
            if (prod.removeStock(quantity)):
                o.save()
        except:
            raise Exception("Couldn't Add Product to Order")

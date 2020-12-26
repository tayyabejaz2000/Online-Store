from ..models import Order
from .product import product
from .orderedproduct import orderedproduct
from .invoice import invoice


class order(Order):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Order):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    def addProduct(self, prod: product, quantity):
        try:
            o = orderedproduct(order=self, product=prod, quantity=quantity)
            prod.stock -= quantity
            prod.removeStock(quantity)
            o.save()
        except:
            raise Exception("Couldn't Add Product to Order")

    def createInvoice(self, discount=0):
        try:
            net = 0
            i = invoice(net=net, discount=discount)

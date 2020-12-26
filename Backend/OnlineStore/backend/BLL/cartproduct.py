from ..models import CartProductModel


class cartproduct:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], CartProductModel):
            self.data = args[0]
        else:
            self.data = CartProductModel(*args, **kwargs)

    @property
    def price(self):
        return self.data.product.price

    @property
    def discount(self):
        return self.data.product.discount

    def getCart(self):
        return self.data.cart

    def setCart(self, cart):
        self.data.cart = cart
    cart = property(getCart, setCart)

    def getProduct(self):
        return self.data.product

    def setProduct(self, prod):
        self.data.product = prod
    product = property(getProduct, setProduct)

    def getQuantity(self):
        return self.data.quantity

    def setQuantity(self, value):
        self.data.quantity = value

    quantity = property(getQuantity, setQuantity)

    def save(self):
        self.data.save()

from .user import user
from .cart import cart
from .billingaddress import billingAddress


class buyer(user):
    def __init__(self, *args, **kwargs) -> None:
        if isinstance(args[0], user):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
            c = cart(buyer=self)
            c.save()

    @property
    def Cart(self) -> cart:
        return cart(self.cart)

    @property
    def Orders(self):
        return self.orders

    @property
    def BillingAddresses(self):
        return self.billing_addresses

    @property
    def Reviews(self):
        return self.reviews

    def addProductToCart(self, product, quantity):
        self.Cart.addProduct(product, quantity)

    def addBillingAddress(self, billingaddress):
        try:
            address = billingAddress(user=self,
                                     billingAddress=billingaddress)
            address.save()
        except:
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingaddress))

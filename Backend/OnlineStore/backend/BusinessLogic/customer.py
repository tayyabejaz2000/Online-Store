from .user import user
from .cart import cart


class customer(user):
    def __init__(self, *args, **kwargs) -> None:
        if isinstance(args[0], user):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

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

    def addBillingAddress(self, billingAddress):
        try:
            address = billingAddress(user=self,
                                     billingAddress=billingAddress)
            address.save()
        except:
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingAddress))

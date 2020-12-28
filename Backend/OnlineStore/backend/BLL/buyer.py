from abc import abstractmethod
from .user import user
from .cart import cart
from .billingaddress import billingAddress


class buyer(user):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], user):
            self.data = args[0].data
        else:
            super().__init__(*args, **kwargs)

    @property
    def cart(self):
        return cart(self.data.cart)

    @property
    def orders(self):
        return self.data.orders

    @property
    def billing_addresses(self):
        return self.data.billing_addresses

    @property
    def reviews(self):
        return self.data.reviews

    def create_cart(self):
        c = cart(buyer=self.data)
        c.save()

    def addProductToCart(self, product, quantity):
        self.cart.addProduct(product, quantity)

    def updateCart(self, product, quantity):
        self.cart.updateProduct(product, quantity)

    def addBillingAddress(self, billingaddress):
        try:
            address = billingAddress(buyer=self.data,
                                     billingAddress=billingaddress)
            address.save()
        except Exception as e:
            print(e)
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingaddress))

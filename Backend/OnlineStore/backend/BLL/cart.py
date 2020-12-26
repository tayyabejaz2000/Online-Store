from .product import product
from ..models import CartModel
from .cartproduct import cartproduct


class cart:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], CartModel):
            self.data = args[0]
        else:
            self.data = CartModel(*args, **kwargs)

    def setbuyer(self, value):
        self.data.buyer = value

    def getBuyer(self):
        return self.data.buyer
    buyer = property(getBuyer, setbuyer)

    @property
    def products(self):
        return self.data.products

    @property
    def cartProducts(self):
        return self.data.cart_products

    @property
    def netTotal(self):
        net = 0
        cart_products = self.cartProducts.all()
        for cart_product in cart_products:
            prod = product(cart_product.product)
            if (cart_product.quantity <= prod.stock):
                net += cart_product.quantity * (prod.price -
                                                (prod.price * (prod.discount/100)))
        return net

    def addProduct(self, product, quantity):
        try:
            c = cartproduct(cart=self.data, product=product, quantity=quantity)
            c.save()
        except:
            raise Exception("Unable to add Product to Cart")

    def removeProduct(self, product):
        try:
            self.cartProducts.filter(product=product).delete()
        except:
            raise Exception("Couldn't delete Cart Product")

    def save(self):
        self.data.save()

from Backend.OnlineStore.backend.BusinessLogic.product import product
from ..models import Cart
from .cartproduct import cartproduct


class cart(Cart):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Cart):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @property
    def cartProducts(self):
        return self.cart_products

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
            c = cartproduct(cart=self, product=product, quantity=quantity)
            c.save()
        except:
            raise Exception("Unable to add Product to Cart")

    def removeProduct(self, product):
        try:
            cart_products = self.cartProducts
            cart_products.filter(product=product).delete()
        except:
            raise Exception("Couldn't delete Cart Product")

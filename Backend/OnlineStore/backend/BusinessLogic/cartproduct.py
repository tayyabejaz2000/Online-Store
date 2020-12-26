from ..models import CartProduct


class cartproduct(CartProduct):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], CartProduct):
            self = CartProduct
        else:
            super().__init__(*args, **kwargs)

    @property
    def price(self):
        return self.product.price

    @property
    def discount(self):
        return self.product.discount

from typing import Dict
from django.forms.models import model_to_dict
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
            cartProducts = self.cartProducts
            # isUnique, always return 1 object
            check = cartProducts.filter(product=product).first()
            if (check is None):
                c = cartproduct(cart=self.data, product=product,
                                quantity=quantity)
                c.save()
            else:
                check.quantity += quantity
                check.save()
        except Exception as e:
            print("Exception Thrown: ", e)
            raise Exception("Unable to add Product to Cart")

    def updateProduct(self, product, quantity):
        try:
            cart_product = cartproduct.get(cart=self.data, product=product)
            cart_product.quantity = quantity
            cart_product.save()
        except Exception as e:
            print("Exception Thrown: ", e)
            raise Exception("Unable to update Product in Cart")

    def getCartData(self):
        CartData = []
        cart_products = self.cartProducts.all()
        for cart_product in cart_products:
            cart_product_data = model_to_dict(cart_product)
            cart_product_data["product"] = model_to_dict(
                cart_product.product)
            CartData.append(cart_product_data)
        return CartData, self.netTotal

    def removeProduct(self, product):
        try:
            cartProduct = self.cartProducts.filter(product=product.data)
            cartProduct.delete()
        except:
            raise Exception("Couldn't delete Cart Product")

    def save(self):
        self.data.save()

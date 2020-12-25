from ..models import UserAccount, Order, Cart, OrderedProduct, Shipping


class orders:
    def placeOrder(self, account: UserAccount):
        order = Order(account=account)
        cartProducts = Cart.products.all()
        net = 0
        for i in cartProducts:
            shipping = Shipping(address=i.product.shop.location)
            shipping.save()
            op = OrderedProduct(
                product=i.product, quantity=i.quantity, order=order, shipping=shipping)
            order.ordered_products.product = i.product
            net += i.product.p

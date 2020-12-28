from django.forms.models import model_to_dict
from .order import order
from .buyer import buyer
from .product import product
from .invoice import invoice


class orders:
    def all(self):
        order.all()

    def get(self, *args, **kwargs):
        order.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        order.filter(*args, **kwargs)

    def placeOrder(self, buyer: buyer, discount: int, billingAddress):
        cart = buyer.cart
        wallet = buyer.wallet
        net = cart.netTotal
        i = invoice(net=net, discount=discount)
        if (wallet.balance < net):
            raise Exception("Wallet low on Balance, Recharge")
        i.save()
        o = order(buyer=buyer.data, invoice=i.data, address=billingAddress)
        o.save()
        cart_products = cart.cartProducts.all()
        for cart_product in cart_products:
            prod = product(cart_product.product)
            o.addProduct(prod, cart_product.quantity)
            cart.removeProduct(prod)
        wallet.removeBalance(net)

    def cancelOrder(self, buyer: buyer, order_id):
        o = order(order.get(pk=order_id))
        i = invoice(o.data.invoice)
        buyer.addBalance(i.total)
        ordered_products = o.data.products.all()
        for ordered_product in ordered_products:
            ordered_product.product.stock += ordered_product.quantity
        i.delete()

    def getOrders(self, buyer: buyer):
        ordered_products = []
        orders = buyer.orders.all()
        for order in orders:
            o = model_to_dict(order)
            o["invoice"] = model_to_dict(order.invoice)
            o["ordered_products"] = []
            orderedProducts = order.products.all()
            for orderedProduct in orderedProducts:
                op = model_to_dict(orderedProduct)
                op["product"] = model_to_dict(orderedProduct.product)
                o["ordered_products"].append(op)
            ordered_products.append(o)
        return ordered_products

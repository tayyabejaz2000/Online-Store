from .BL_Data import SHOP_CUT
from .wallet import wallet
from .invoice import invoice
from .product import product
from .buyer import buyer
from .order import order
from .orderedproduct import orderedproduct
from django.forms.models import model_to_dict


class orders:
    def all(self):
        order.all()

    def get(self, *args, **kwargs):
        order.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        order.filter(*args, **kwargs)

    def placeOrder(self, buyer: buyer, discount: int, billingAddress):
        cart = buyer.cart
        buyer_wallet = buyer.wallet
        net = cart.netTotal
        i = invoice(net=net, discount=discount)
        if (buyer_wallet.balance < net):
            raise Exception("Wallet low on Balance, Recharge")
        i.save()
        o = order(buyer=buyer.data, invoice=i.data, address=billingAddress)
        o.save()
        cart_products = cart.cartProducts.all()
        for cart_product in cart_products:
            prod = product(cart_product.product)
            seller_wallet = wallet(prod.shop.seller.wallet)
            net = prod.net * cart_product.quantity
            seller_profit = net - (net * SHOP_CUT/100)
            seller_wallet.addBalance(seller_profit)
            o.addProduct(prod, cart_product.quantity)
            cart.removeProduct(prod)
        buyer_wallet.removeBalance(net)

    def cancelOrderItem(self, buyer: buyer, ordered_product_id):
        o = orderedproduct.get(pk=ordered_product_id)
        prod = product(o.product)
        prod.stock += o.quantity
        prod.save()
        o.delete()
        inv = o.order.invoice
        inv.net -= prod.net
        inv.save()
        buyer.addBalance(prod.net)

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

    def returnItem(self, buyer: buyer, ordered_product_id):
        o = orderedproduct.get(pk=ordered_product_id)
        prod = product(o.product)
        prod.stock += o.quantity
        o.status = 'R'
        prod.save()
        o.save()
        buyer.addBalance(prod.net)

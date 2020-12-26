from .order import order
from .buyer import buyer
from .product import product
from .invoice import invoice
from .orderedproduct import orderedproduct
from .billingaddress import billingAddress


class orders:
    def placeOrder(self, buyer: buyer, discount: int, billingAddress: billingAddress):
        cart = buyer.cart
        wallet = buyer.wallet
        net = cart.netTotal
        i = invoice(net=net, discount=discount)
        if (wallet.balance < net):
            raise Exception("Wallet low on Balance, Recharge")
        i.save()
        o = order(buyer=buyer, invoice=i, address=billingAddress)
        o.save()
        cart_products = cart.cartProducts
        for cart_product in cart_products:
            prod = product(cart_product.product)
            o.addProduct(prod, cart_product.quantity)
            cart.removeProduct(prod)
        wallet.removeBalance(net)

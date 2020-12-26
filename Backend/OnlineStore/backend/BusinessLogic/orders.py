from .order import order
from .buyer import buyer
from .product import product
from .invoice import invoice
from .orderedproduct import orderedproduct
from .billingaddress import billingAddress


class orders:
    def placeOrder(self, buyer: buyer, discount: int, billingAddress: billingAddress):
        cart = buyer.Cart
        wallet = buyer.Wallet
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
            if(prod.removeStock(cart_product.quantity)):
                cart.removeProduct(prod)
                orderedProduct = orderedproduct(order=o, product=prod,
                                                quantity=cart_product.quantity)
                orderedProduct.save()

        wallet.removeBalance(net)

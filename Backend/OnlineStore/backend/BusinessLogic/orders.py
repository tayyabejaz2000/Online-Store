from ..models import BillingAddress, Invoice, UserAccount, Order, OrderedProduct, Shipping
from .user import user


class orders:
    def placeOrder(self, User: user, discount: int, billingAddress: BillingAddress):
        cart = User.getCart()
        wallet = User.getWallet()
        netTotal = cart.netTotal
        invoice = Invoice(net=netTotal, discount=discount)
        if (invoice.total > wallet.balance):
            raise Exception("Account Balance is low. Recharge Now")
        User.removeBalance(invoice.total)
        order = Order(account=User.account, invoice=invoice)
        invoice.save()
        order.save()
        cartProducts = cart.cart_products.all()
        for cartProduct in cartProducts:
            product = cartProduct.product
            if (cartProduct.quantity <= product.stock):
                shipping = Shipping(address=billingAddress)
                op = OrderedProduct(product=product, quantity=cartProduct.quantity,
                                    order=order, shipping=shipping)
                product.stock -= cartProduct.quantity
                product.save()
                shipping.save()
                op.save()
                cartProduct.delete()

from ..models import BillingAddress, CartProduct


class user:

    def __init__(self, account):
        self.account = account

    def addBillingAddress(self, billingAddress):
        try:
            address = BillingAddress(user=self.account,
                                     billingAddress=billingAddress)
            address.save()
        except:
            raise Exception("Couldn't add address for User, [Address]:" +
                            str(billingAddress))

    def getCart(self):
        return self.account.cart

    def addProductToCart(self, product, quantity):
        try:
            cart = self.getCart()
            CartEntry = CartProduct(cart=cart, product=product,
                                    quantity=quantity)
            CartEntry.save()
        except:
            raise Exception("Unable to add Product to Cart")

    def authWallet(self, password):
        wallet = self.account.wallet
        return wallet.check_password(password)

    def addBalance(self, balance):
        wallet = self.account.wallet
        wallet.balance += balance
        wallet.save()

    def removeBalance(self, balance):
        wallet = self.account.wallet
        wallet.balance -= balance
        wallet.save()

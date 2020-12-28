from ..models import WalletModel


class wallet:
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], WalletModel):
            self.data = args[0]
        else:
            self.data = WalletModel(*args, **kwargs)

    def getBalance(self):
        return self.data.balance

    def setBalance(self, value):
        self.data.balance = value
    balance = property(getBalance, setBalance)

    def authWallet(self, password):
        return self.data.check_password(password)

    def setPassword(self, password):
        self.data.set_password(password)
        self.save()

    def addBalance(self, balance):
        self.balance += balance
        self.save()

    def removeBalance(self, balance):
        self.balance -= balance
        self.save()

    def save(self):
        self.data.save()

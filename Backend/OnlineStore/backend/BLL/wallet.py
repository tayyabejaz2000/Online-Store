from ..models import WalletModel


class wallet(WalletModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], WalletModel):
            self.data = args[0]
        else:
            self.data = WalletModel(*args, **kwargs)

    def authWallet(self, password):
        return self.data.check_password(password)

    def addBalance(self, balance):
        self.balance += balance
        self.save()

    def removeBalance(self, balance):
        self.balance -= balance
        self.save()

    def save(self):
        self.data.save()

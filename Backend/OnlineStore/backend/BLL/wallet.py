from ..models import WalletModel


class wallet(WalletModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], WalletModel):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    def authWallet(self, password):
        return self.check_password(password)

    def addBalance(self, balance):
        self.balance += balance
        self.save()

    def removeBalance(self, balance):
        self.balance -= balance
        self.save()

    class Meta:
        abstract = True

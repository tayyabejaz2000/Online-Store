from ..models import Wallet


class wallet(Wallet):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Wallet):
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

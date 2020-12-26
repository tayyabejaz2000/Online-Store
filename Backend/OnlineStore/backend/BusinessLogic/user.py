from .account import account
from .wallet import wallet


class user(account):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], account):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @property
    def Wallet(self) -> wallet:
        return wallet(self.wallet)

    @property
    def Complaints(self):
        return self.complaints

    def authWallet(self, password):
        return self.Wallet.check_password(password)

    def addBalance(self, balance):
        self.Wallet.addBalance(balance)

    def removeBalance(self, balance):
        self.Wallet.removeBalance(balance)

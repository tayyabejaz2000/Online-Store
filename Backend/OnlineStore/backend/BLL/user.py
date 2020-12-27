from .account import account
from .wallet import wallet


class user(account):

    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], account):
            self.data = args[0].data
        else:
            super().__init__(*args, **kwargs)

    def create_wallet(self, wallet_password):
        w = wallet(user=self.data)
        if wallet_password is not None:
            w.data.set_password(wallet_password)
        w.save()

    @property
    def wallet(self) -> wallet:
        return wallet(self.data.wallet)

    @property
    def complaints(self):
        return self.data.complaints

    def authWallet(self, password):
        return self.wallet.check_password(password)

    def addBalance(self, balance):
        self.wallet.addBalance(balance)

    def removeBalance(self, balance):
        self.wallet.removeBalance(balance)

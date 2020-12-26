from .account import account
from .wallet import wallet
import copy


class user(account):

    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], account):
            self.data = args[0]
        else:
            super().__init__(*args, **kwargs)
            w = wallet(user=self)
            wallet_password = kwargs.pop("wallet_password", None)
            if wallet_password is not None:
                w.set_password(wallet_password)
            w.save()

    @property
    def wallet(self) -> wallet:
        return wallet(self.data.wallet)

    @property
    def complaints(self):
        return self.data.complaints

    def authWallet(self, password):
        return self.Wallet.check_password(password)

    def addBalance(self, balance):
        self.Wallet.addBalance(balance)

    def removeBalance(self, balance):
        self.Wallet.removeBalance(balance)

    class Meta:
        abstract = True

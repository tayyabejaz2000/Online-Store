from ..models import Wallet, UserAccount


class wallets:
    def addBalance(self, user_id, balance):
        user = UserAccount.objects.get(pk=user_id)
        wallet = Wallet.objects.get(user=user)
        wallet.balance += balance
        wallet.save()

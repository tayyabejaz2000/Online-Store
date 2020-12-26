from ..models import UserAccount
from .shop import shop
from .wallet import wallet
from .user import user


class vendor(user):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], user):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @property
    def Shop(self) -> shop:
        return self.shop

    def editShop(self, shop_name, shop_location):
        self.Shop.edit(shop_name, shop_location)

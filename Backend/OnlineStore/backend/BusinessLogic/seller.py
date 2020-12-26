from ..models import UserAccount
from .shop import shop
from .wallet import wallet
from .user import user


class seller(user):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], user):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)
            shop_name = kwargs.pop("shop_name", None)
            shop_location = kwargs.pop("shop_location", None)
            s = shop(seller=self, name=shop_name, location=shop_location)
            s.save()

    @property
    def Shop(self) -> shop:
        return shop(self.shop)

    def editShop(self, shop_name, shop_location):
        self.Shop.edit(shop_name, shop_location)

from .shop import shop
from .user import user


class seller(user):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], user):
            self.data = args[0].data
        else:
            super().__init__(*args, **kwargs)

    @property
    def shop(self) -> shop:
        return shop(self.data.shop)

    def create_shop(self, shop_name, shop_location):
        s = shop(seller=self.data, name=shop_name, location=shop_location)
        s.save()

    def editShop(self, shop_name, shop_location):
        self.shop.edit(shop_name, shop_location)

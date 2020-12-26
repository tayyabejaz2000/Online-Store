from ..models import ShopModel


class shop(ShopModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ShopModel):
            self.data = args[0]
        else:
            self.data = ShopModel(*args, **kwargs)

    @property
    def products(self):
        return self.data.products

    def edit(self, shop_name, shop_location):
        try:
            self.name = shop_name
            self.location = shop_location
            self.save()
        except:
            raise Exception("Couldn't Edit Shop Object")

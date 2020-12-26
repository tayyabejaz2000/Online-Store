from ..models import Shop


class shop(Shop):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], Shop):
            self = args[0]
        else:
            super().__init__(*args, **kwargs)

    @property
    def Products(self):
        return self.products

    def edit(self, shop_name, shop_location):
        try:
            self.name = shop_name
            self.location = shop_location
            self.save()
        except:
            raise Exception("Couldn't Edit Shop Object")

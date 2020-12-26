from ..models import ShopModel


class shop(ShopModel):
    def __init__(self, *args, **kwargs):
        if len(args) > 0 and isinstance(args[0], ShopModel):
            self.data = args[0]
        else:
            self.data = ShopModel(*args, **kwargs)

    def __dict__(self):
        return {
            "seller": self.seller.pk,
            "name": self.name,
            "location": self.location,
        }

    @property
    def products(self):
        return self.data.products

    @property
    def seller(self):
        return self.data.seller

    def edit(self, shop_name, shop_location):
        try:
            self.name = shop_name
            self.location = shop_location
            self.save()
        except:
            raise Exception("Couldn't Edit Shop Object")

    def save(self):
        self.data.save()

    def getName(self):
        return self.data.name

    def setName(self, value):
        self.data.name = value
    name = property(getName, setName)

    def getLocation(self):
        return self.data.location

    def setLocation(self, value):
        self.data.location = value
    location = property(getLocation, setLocation)

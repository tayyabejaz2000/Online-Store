class vendor:

    def __init__(self, account):
        self.account = account

    def editShop(self, shop_name, shop_location):
        try:
            shop = self.account.shop
            shop.name = shop_name
            shop.location = shop_location
            shop.save()
        except:
            raise Exception("Couldn't add Shop for Vendor, [Shop Name]:" +
                            str(shop_name) + ", [Shop Location]:" + str(shop_location))

    def getShop(self):
        return self.account.shop

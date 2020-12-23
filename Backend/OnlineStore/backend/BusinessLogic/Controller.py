from .Accounts import Accounts, User, Vendor


class Store:
    def __init__(self):
        self.accounts = Accounts()
        self.vendors = Vendor()
        self.users = User()

    def login_user(self):
        return self.accounts.login_user()

    def create_user(self, user_data):
        self.accounts.create_user(user_data)

    def logout_user(self, token):
        self.accounts.logout_user(token)

    def addBillingAddress(self, user_id, address):
        user = self.accounts.getAccount(user_id)
        self.users.addBillingAddress(user, address)

    def setShop(self, vendor_id, shop_name, shop_location):
        vendor = self.accounts.getAccount(vendor_id)
        self.vendors.setShop(vendor, shop_name, shop_location)

    def addProduct(self, vendor_id, product_name, product_desc, quantity):
        vendor = self.accounts.getAccount(vendor_id)
        shop = vendor.shop
        self.vendors.addProduct(shop, product_name,
                                product_desc, quantity)

    def removeProduct(self, product_id):
        self.vendors.removeProduct(product_id)

    def getAllProducts(self):
        returnVal = {
            "Products": [
                [{
                    "name": "hello",
                }],
                [{
                    "name": "hello",
                }],
                [{
                    "name": "hello",
                }]
            ]
        }

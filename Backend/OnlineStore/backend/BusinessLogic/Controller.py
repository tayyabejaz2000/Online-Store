from Backend.OnlineStore.backend.BusinessLogic.complaints import complaints
from .accounts import accounts
from .products import products
from .user import user
from .vendor import vendor


class Store:
    def __init__(self):
        self.accounts = accounts()
        self.products = products()
        self.complaints = complaints()

    # accounts.py functions

    def login_user(self):
        return self.accounts.login_user()

    def create_user(self, user_data):
        self.accounts.create_user(user_data)

    def logout_user(self, token):
        self.accounts.logout_user(token)

    def getAccountData(self, account_id):
        account = self.accounts.getAccount(account_id)
        return {
            "username": account.username,
            "accountType": account.user_type,
        }

    # user.py functions

    def addBillingAddress(self, account_id, address):
        account = self.accounts.getAccount(account_id)
        User = user(account)
        User.addBillingAddress(address)

    def addProductToCart(self, account_id, product_id, quantity):
        account = self.accounts.getAccount(account_id)
        product = self.products.getProduct(product_id)
        User = user(account)
        User.addProductToCart(product, quantity)

    # vendor.py functions

    def editShop(self, account_id, shop_name, shop_location):
        account = self.accounts.getAccount(account_id)
        Vendor = vendor(account)
        Vendor.editShop(shop_name, shop_location)

    # products.py functions

    def addProduct(self, account_id, product_name, product_desc, quantity, category, price):
        account = self.accounts.getAccount(account_id)
        Vendor = vendor(account)
        shop = Vendor.getShop()
        self.products.addProduct(product_name, product_desc, quantity,
                                 category, shop, price)

    def removeProduct(self, product_id):
        self.products.removeProduct(product_id)

    def getAllProducts(self):
        products = self.products.getAllProducts()
        return {"products": products}

    def updateProduct(self, product_id, product_name, product_desc, quantity, category, price):
        self.products.updateProduct(product_id, product_name,
                                    product_desc, quantity, category, price)

    def addReview(self, account_id, product_id, stars, feedback):
        account = self.accounts.getAccount(account_id)
        product = self.products.getProduct(product_id)
        self.products.addReview(account, product, stars, feedback)

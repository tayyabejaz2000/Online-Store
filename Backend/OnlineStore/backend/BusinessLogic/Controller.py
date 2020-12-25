from Backend.OnlineStore.backend.BusinessLogic.complaints import complaints
from .accounts import accounts
from .products import products
from .user import user
from .vendor import vendor
from .orders import orders


class Store:
    def __init__(self):
        self.accounts = accounts()
        self.products = products()
        self.complaints = complaints()
        self.orders = orders()

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

    def getCart(self, account_id):
        account = self.accounts.getAccount(account_id)
        User = user(account)
        cart = User.getCart()
        return cart

    def addProductToCart(self, account_id, product_id, quantity):
        account = self.accounts.getAccount(account_id)
        product = self.products.getProduct(product_id)
        User = user(account)
        User.addProductToCart(product, quantity)

    def addBalance(self, account_id, balance, password):
        account = self.accounts.getAccount(account_id)
        User = user(account)
        if User.authWallet(password):
            User.addBalance(balance=balance)
        else:
            raise Exception("Invalid Wallet Password!")

    def removeBalance(self, account_id, balance, password):
        account = self.accounts.getAccount(account_id)
        User = user(account)
        if User.authWallet(password):
            User.removeBalance(balance=balance)
        else:
            raise Exception("Invalid Wallet Password!")

    # vendor.py functions

    def editShop(self, account_id, shop_name, shop_location):
        account = self.accounts.getAccount(account_id)
        Vendor = vendor(account)
        Vendor.editShop(shop_name, shop_location)

    def getShop(self, account_id):
        account = self.accounts.getAccount(account_id)
        Vendor = vendor(account)
        return Vendor.getShop()  # confirm return

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

    # complaints.py
    def addComplaint(self, account_id, complaint_body):
        account = self.accounts.getAccount(account_id)
        self.complaints.addComplaint(account, complaint_body)

    def getAllComplaints(self):
        return self.complaints.getAllComplaints()

    def resolveComplaint(self, complaint_id, account_id, response):
        account = self.accounts.getAccount(account_id)
        self.complaints.resolveComplaint(complaint_id, account, response)

    # orders.py

    # Controller Functions

    def getComplaints(self, account_id):
        account = self.accounts.getAccount(account_id)
        return account.complaints

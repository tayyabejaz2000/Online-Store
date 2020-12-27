from .accounts import accounts, account
from .employee import employee
from .user import user
from .buyer import buyer
from .seller import seller
from .products import products
from .orders import orders
from .complaints import complaints


class Store:
    def __init__(self):
        self.accounts = accounts()
        self.products = products()
        self.complaints = complaints()
        self.orders = orders()

    # accounts.py functions

    def login_account(self):
        return self.accounts.login_account()

    def create_account(self, user_data):
        if user_data["user_type"] == 'B':
            self.accounts.create_buyer_account(user_data["username"], user_data["password"], user_data["email"],
                                               user_data["first_name"], user_data["last_name"], user_data["user_type"],
                                               user_data["phone_number"], user_data["wallet_password"])
        elif user_data["user_type"] == 'S':
            self.accounts.create_seller_account(user_data["username"], user_data["password"], user_data["email"],
                                                user_data["first_name"], user_data["last_name"], user_data["user_type"],
                                                user_data["phone_number"], user_data["wallet_password"], user_data["shop_name"],
                                                user_data["shop_location"])
        else:
            self.accounts.create_account(user_data["username"], user_data["password"], user_data["email"],
                                         user_data["first_name"], user_data["last_name"], user_data["user_type"],
                                         user_data["phone_number"])

    def logout_account(self, token):
        self.accounts.logout_account(token)

    def getAccountData(self, account_id):
        a = self.accounts.get(pk=account_id)
        return {
            "username": a.username,
            "user_type": a.user_type,
        }

    # user.py functions

    def addBillingAddress(self, buyer_id, address):
        a = buyer(self.accounts.get(pk=buyer_id))
        a.addBillingAddress(address)

    def addProductToCart(self, buyer_id, product_id, quantity):
        b = buyer(self.accounts.get(pk=buyer_id))
        p = self.products.get(pk=product_id)
        b.addProductToCart(p, quantity)

    def addBalance(self, user_id, balance, wallet_password):
        u = user(self.accounts.get(pk=user_id))
        if u.wallet.authWallet(wallet_password):
            u.addBalance(balance)
        else:
            raise Exception("Invalid Wallet Password!")

    def removeBalance(self, user_id, balance, wallet_password):
        u = user(self.accounts.get(pk=user_id))
        if u.wallet.authWallet(wallet_password):
            u.removeBalance(balance)
        else:
            raise Exception("Invalid Wallet Password!")

    # seller.py functions

    def editShop(self, seller_id, shop_name, shop_location):
        s = seller(self.accounts.get(pk=seller_id))
        s.editShop(shop_name, shop_location)

    def getShop(self, seller_id):
        s = seller(self.accounts.get(pk=seller_id))
        return s.shop.__dict__()

    def getSellerProducts(self, seller_id):
        s = seller(self.accounts.get(pk=seller_id))
        products = s.shop.products
        return {
            "products": list(products.filter(isRemoved=False).values())
        }
    # products.py functions

    def addProduct(self, seller_id, product_name, product_desc, quantity, price, discount, category_name):
        s = seller(self.accounts.get(pk=seller_id))
        self.products.addProduct(product_name, product_desc, quantity, price,
                                 discount, category_name, s)

    def removeProduct(self, product_id):
        self.products.removeProduct(product_id)

    def getAllProducts(self):
        products = self.products.all()
        return {"products": list(products.values())}

    def updateProduct(self, product_id, product_name, product_desc, quantity, price, discount, category_name):
        self.products.updateProduct(product_id, product_name, product_desc, quantity,
                                    price, discount, category_name)

    def addReview(self, buyer_id, product_id, stars, feedback):
        b = buyer(self.accounts.get(pk=buyer_id))
        self.products.addReview(b, product_id, stars, feedback)

    # complaints.py
    def addComplaint(self, user_id, complaint_body):
        u = user(self.accounts.get(pk=user_id))
        self.complaints.addComplaint(u, complaint_body)

    def getAllComplaints(self):
        return self.complaints.all()

    def resolveComplaint(self, complaint_id, employee_id, response):
        e = employee(account(self.accounts.get(pk=employee_id)))
        self.complaints.resolveComplaint(complaint_id, e, response)

    # Controller Functions

    def getComplaints(self, user_id):
        u = user(account(self.accounts.get(pk=user_id)))
        return u.complaints
    # Add Rest Created Functions in Controller

    def getAllCategories(self):
        categories = self.products.categories.all()
        return {
            "categories": list(categories.values())
        }

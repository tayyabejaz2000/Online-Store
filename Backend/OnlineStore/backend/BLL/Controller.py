from .accounts import accounts, account
from .employee import employee
from .user import user
from .buyer import buyer
from .seller import seller
from .products import products
from .orders import orders
from .complaints import complaints
from django.forms.models import model_to_dict


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

    def editUser(self, account_id, username, password, email, first_name, last_name, phone_number, wallet_password):
        u = user(self.accounts.get(pk=account_id))
        u.editAccount(username, password, email,
                      first_name, last_name, phone_number)
        if wallet_password is not None:
            u.setWalletPassword(wallet_password)

    def logout_account(self, token):
        self.accounts.logout_account(token)

    def getAccountData(self, account_id):
        a = self.accounts.get(pk=account_id)
        return {
            "username": a.username,
            "user_type": a.user_type,
        }

    def getAccountDetails(self, account_id):
        a = self.accounts.get(pk=account_id)
        account_details = model_to_dict(a)
        account_details.pop("password")
        return account_details

    # user.py functions

    def addBillingAddress(self, buyer_id, address):
        a = buyer(self.accounts.get(pk=buyer_id))
        a.addBillingAddress(address)

    def getBillingAddresses(self, buyer_id):
        a = buyer(self.accounts.get(pk=buyer_id))
        return {"billing_addresses": list(a.billing_addresses.all().values())}

    def addProductToCart(self, buyer_id, product_id, quantity):
        b = buyer(self.accounts.get(pk=buyer_id))
        p = self.products.get(pk=product_id)
        b.addProductToCart(p, quantity)

    def updateCart(self, buyer_id, product_id, quantity):
        b = buyer(self.accounts.get(pk=buyer_id))
        p = self.products.get(pk=product_id)
        b.updateCart(p, quantity)

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
        return model_to_dict(s.shop.data)

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

    def getProduct(self, product_id):
        product = self.products.get(pk=product_id)
        return model_to_dict(product)

    def removeProduct(self, product_id):
        self.products.removeProduct(product_id)

    def getAllProducts(self):
        products = self.products.filter(isRemoved=False)
        return {"products": list(products.values())}

    def updateProduct(self, product_id, product_name, product_desc, quantity, price, discount, category_name):
        self.products.updateProduct(product_id, product_name, product_desc, quantity,
                                    price, discount, category_name)

    def addReview(self, buyer_id, product_id, stars, feedback):
        b = buyer(self.accounts.get(pk=buyer_id))
        prod = self.products.get(pk=product_id)
        self.products.addReview(b, prod, stars, feedback)

    # complaints.py
    def addComplaint(self, user_id, complaint_body):
        u = user(self.accounts.get(pk=user_id))
        self.complaints.addComplaint(u, complaint_body)

    def getAllComplaints(self):
        return self.complaints.all()

    def resolveComplaint(self, complaint_id, employee_id, response):
        e = employee(self.accounts.get(pk=employee_id))
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

    def getCartProducts(self, buyer_id):
        b = buyer(self.accounts.get(pk=buyer_id))
        cartData = b.cart.getCartData()
        return {"products": cartData[0], "total": cartData[1]}

    def placeOrder(self, buyer_id, billing_address, discount, wallet_password):
        b = buyer(self.accounts.get(pk=buyer_id))
        if (b.wallet.authWallet(wallet_password)):
            billingAddress = b.billing_addresses.filter(
                billingAddress=billing_address).first()
            self.orders.placeOrder(b, discount, billingAddress)

    def cancelOrderItem(self, buyer_id, ordered_item_id):
        b = buyer(self.accounts.get(pk=buyer_id))
        self.orders.cancelOrderItem(b, ordered_item_id)

    def getOrders(self, buyer_id):
        b = buyer(self.accounts.get(pk=buyer_id))
        orders = self.orders.getOrders(b)
        return orders

    def returnItem(self, buyer_id, ordered_product_id):
        b = buyer(self.accounts.get(pk=buyer_id))
        self.orders.returnItem(b, ordered_product_id)

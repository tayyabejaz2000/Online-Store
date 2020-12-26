from .account import account
from .buyer import buyer
from .seller import seller
from .tokenHandler import JWTAccountHandeling


class accounts:

    def all(self):
        return account.all()

    def get(self, *args, **kwargs):
        return account.get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return account.filter(*args, **kwargs)

    def create_account(self, username, password, email, first_name, last_name, user_type, phone_number):
        try:
            a = account(username=username, password=password, email=email, first_name=first_name,
                        last_name=last_name, user_type=user_type, phone_number=phone_number)
            a.save()
        except:
            raise Exception("Couldn't create Account")

    def create_buyer_account(self, username, password, email, first_name, last_name, user_type, phone_number, wallet_password):
        try:
            b = buyer(username=username, password=password, email=email, first_name=first_name,
                      last_name=last_name, user_type=user_type, phone_number=phone_number)
            b.create_wallet(wallet_password)
            b.create_cart()
            b.save()
        except:
            raise Exception("Couldn't create Buyer Account")

    def create_seller_account(self, username, password, email, first_name, last_name, user_type,
                              phone_number, wallet_password, shop_name, shop_location):
        try:
            s = seller(username=username, password=password, email=email, first_name=first_name,
                       last_name=last_name, user_type=user_type, phone_number=phone_number)
            s.create_wallet(wallet_password)
            s.create_shop(shop_name, shop_location)
            s.save()
        except:
            raise Exception("Couldn't create Seller Account")

    def login_account(self):
        return JWTAccountHandeling.login_account()

    def logout_account(self, refresh_token):
        return JWTAccountHandeling.logout_account(refresh_token)

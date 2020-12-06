from abc import abstractmethod
from ..views import AccountCreate, ObtainTokenWithCustomClaims, LogoutAndBlacklistToken
from rest_framework_simplejwt import views as jwt_views


class AccountHandler:
    @abstractmethod
    def login_user(self):
        pass

    @abstractmethod
    def logout_user(self):
        pass

    @abstractmethod
    def create_user(self):
        pass


class TokenizedAccountHandler(AccountHandler):
    def login_user(self):
        return ObtainTokenWithCustomClaims.as_view()

    def logout_user(self):
        return LogoutAndBlacklistToken().as_view()

    def create_user(self):
        return AccountCreate.as_view()

    def refresh_user_token(self):
        return jwt_views.TokenRefreshView.as_view()

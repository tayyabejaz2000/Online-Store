from django.urls import path
from .BusinessLogic.accountHandler import TokenizedAccountHandler

accountHandler = TokenizedAccountHandler()
urlpatterns = [
    # login and get token
    path('login/', accountHandler.login_user()),
    # refresh from token
    path('refresh/', accountHandler.refresh_user_token()),
    # sign up/create new user
    path('signup/', accountHandler.create_user()),
    # logout
    path('logout/', accountHandler.logout_user()),
]

from django.urls import path
from .views import UserRegistration, UserLogin, ChatAPI, TokenBalanceAPI

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('chat/', ChatAPI.as_view(), name='chat'),
    path('tokens/', TokenBalanceAPI.as_view(), name='token_balance'),
]

from curses.ascii import CR
from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create_user'),
]
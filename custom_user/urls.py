from django.urls import path
from custom_user.views import CustomUser

urlpatterns = [
    path('', CustomUser)
]
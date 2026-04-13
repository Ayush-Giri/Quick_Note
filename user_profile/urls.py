from rest_framework.routers import DefaultRouter
from user_profile.views import UserProfileViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', viewset=UserProfileViewSet, basename="user-profile")


urlpatterns = [
    path('', include(router.urls)),
]


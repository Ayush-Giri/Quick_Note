from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet, CategoryViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'notes', viewset=NoteViewSet, basename="notes")
router.register(r'category', viewset=CategoryViewSet, basename="category")

urlpatterns = [
    path('', include(router.urls))
]

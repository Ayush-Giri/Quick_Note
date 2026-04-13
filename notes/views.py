from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework import permissions
from notes.models import Notes, Category
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from notes.serializers import NotesSerializer, CategorySerializer
from notes.permissions import IsOwnerOrPublicReadOnly

# Create your views here.


class NotePagination(PageNumberPagination):
    page_size=10
    max_page_size = 100
    page_size_query_param = "page_size"
    page_query_param = "page"


class CategoryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NoteViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrPublicReadOnly]
    serializer_class = NotesSerializer
    pagination_class = NotePagination

    def get_queryset(self):
        query_parameters = self.request.query_params
        public = query_parameters.get('public')
        category = query_parameters.get("category")
        queryset = Notes.objects.all()

        if public:
            queryset = queryset.filter(is_public=True)
            if category:
                queryset=queryset.filter(category=category)
        else:
            if category:
                queryset=queryset.filter(user=self.request.user, category=category)
            else:
                queryset=queryset.filter(user=self.request.user)
        
        return queryset


    @action(detail=True, methods=["patch"], url_path="make-public")
    def make_private(self, pk=None):
        instance = self.get_object()
        instance.is_public=True
        instance.save()
        return Response(
            {"message": "note made public"},
            status=status.HTTP_200_OK
        )
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    



from rest_framework.serializers import ModelSerializer
from notes.models import Category, Notes


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


    
class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = [
            'id',
            'user',
            'title',
            'note',
            'category',
            'image_attachments',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'user',
            'created_at',
            'updated_at'
        ]
from rest_framework.serializers import (
    Serializer,
    IntegerField,
    ModelSerializer,
    SerializerMethodField,
)
from post.models import Post
from user.serializers import BasicUserSerializer


class PostWithUserSerializer(ModelSerializer):
    user = BasicUserSerializer()

    class Meta:
        model = Post
        fields = [
            'id', 'body', 'user'
        ]


class PostWithCategoriesCountSerializer(ModelSerializer):
    categories_count = SerializerMethodField()
    user = BasicUserSerializer()

    def get_categories_count(self, obj):
        return obj.categories_count

    class Meta:
        model = Post
        fields = [
            'id', 'body', 'categories_count', 'user'
        ]


class PostGroupByCreatedDaySerializer(Serializer):
    count = IntegerField()
    created_day = IntegerField()

from django.urls import path
from rest_framework.generics import ListAPIView
from django.db.models import Count
from post.models import Post
from .serializers import (
    PostWithUserSerializer,
    PostWithCategoriesCountSerializer,
)

urlpatterns = [
    # selecting the posts with each user
    path(
        'getting-posts-with-users/',
        ListAPIView.as_view(
            queryset=Post.objects.all().prefetch_related('user'),
            serializer_class=PostWithUserSerializer,
        ),
        name='getting-posts-with-users'
    ),

    # getting the categories count for each post and filtering based on that
    path(
        'aggregations-1/',
        ListAPIView.as_view(
            queryset=Post.objects.annotate(
                categories_count=Count('categories')
            ).prefetch_related('user').filter(categories_count__gte=4),
            serializer_class=PostWithCategoriesCountSerializer,
        ),
        name='aggregations-1'
    ),

    # getting the top posts based on the number of categories

    path(
        'aggregations-2/',
        ListAPIView.as_view(
            queryset=Post.objects.annotate(
                categories_count=Count('categories'),
            ).prefetch_related('user').order_by('-categories_count'),
            serializer_class=PostWithCategoriesCountSerializer,
        ),
        name='aggregations-2',
    )
]

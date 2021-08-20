from django.urls import path
from rest_framework.generics import ListAPIView
from django.db.models.functions import ExtractYear, ExtractDay
from django.db.models import Count
from post.models import Post
from .serializers import (
    PostWithUserSerializer,
    PostGroupByCreatedDaySerializer,
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
    ),

    # the posts the have been created in 2015 or later

    path(
        'queying-dates-1/',
        ListAPIView.as_view(
            queryset=Post.objects.annotate(
                created_at_year=ExtractYear('created_at')
            ).filter(created_at_year__gte=2015).prefetch_related('user'),
            serializer_class=PostWithUserSerializer,
        ),
        name='queying-dates-1'
    ),

    # the posts the have been created in 2021, at the first day of any month


    path(
        'queying-dates-2/',
        ListAPIView.as_view(
            queryset=Post.objects.annotate(
                created_at_year=ExtractYear('created_at'),
                created_at_day=ExtractDay('created_at')
            ).filter(
                created_at_year=2021,
                created_at_day=17
            ).prefetch_related('user'),
            serializer_class=PostWithUserSerializer,
        ),
        name='queying-dates-2'
    ),

    # return the count of posts grouped by day

    path(
        'queying-dates-3/',
        ListAPIView.as_view(
            queryset=Post.objects.annotate(
                created_day=ExtractDay('created_at'),
            ).values('created_day').annotate(count=Count('id')),
            serializer_class=PostGroupByCreatedDaySerializer,
            pagination_class=None,
        ),
        name='queying-dates-3'
    ),
]

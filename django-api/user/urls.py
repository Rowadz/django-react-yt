from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import ListAPIView
from django.db.models import Prefetch, Count
from category.models import Category
from post.models import Post
from category.model_enums import CategoryNames
from .views import LoginView, RegisterView
from .models import User
from .serializers import UsersSerializer, UsersSerializer2

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # filter the category based on the name
    path(
        'queries-1/',
        ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related(
                Prefetch(
                    'posts__categories',
                    queryset=Category.objects.filter(name=CategoryNames.CPP)
                )
            ),
            serializer_class=UsersSerializer,
        ),
        name='queries-1'
    ),
    # Getting the posts that have CPP as a category
    path(
        'queries-2/',
        ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related(
                Prefetch(
                    'posts',
                    queryset=Post.objects.filter(
                        categories__name__in=[CategoryNames.CPP]
                    ).prefetch_related('categories')
                )
            ),
            serializer_class=UsersSerializer,
        ),
        name='queries-2'
    ),
    # Filtering based on the relationship count [ONLY having a CPP as a category]
    path(
        'queries-3/',
        ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related(
                Prefetch(
                    'posts',
                    queryset=Post.objects.annotate(categories_count=Count('categories')).filter(
                        categories__name=CategoryNames.CPP,
                        categories_count=1,
                    ).prefetch_related('categories')
                )
            ),
            serializer_class=UsersSerializer,
        ),
        name='queries-3'
    ),
    path(
        'queries-4/',
        ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related(
                Prefetch(
                    'posts',
                    queryset=Post.objects.annotate(categories_count=Count('categories')).filter(
                        categories__name=CategoryNames.CPP,
                        categories_count=1,
                    ).prefetch_related('categories')
                )
            ),
            serializer_class=UsersSerializer,
        ),
        name='queries-4'
    ),
    path(
        'top-10-users-by-post-count/',
        ListAPIView.as_view(
            queryset=User.objects.annotate(
                posts_count=Count('posts')
            ).order_by('-posts_count')[0:10],
            serializer_class=UsersSerializer2,
            pagination_class=None,
        ),
        name='top-10-users-by-post-count',
    )
]

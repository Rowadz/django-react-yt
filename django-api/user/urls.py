from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import ListAPIView
from django.db.models import Prefetch, Count, Q
from django.db.models.functions import Lower
from category.models import Category
from post.models import Post
from category.model_enums import CategoryNames
from .views import LoginView, RegisterView
from .models import User
from .serializers import UsersSerializer, UsersSerializer2, UsersSerializer3

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
    ),

    # select where the first_name = Brittany or last_name = Jacobs
    path(
        'complex-queries-1',
        ListAPIView.as_view(
            queryset=User.objects.filter(
                Q(first_name='Brittany') & Q(last_name='Jacobs')
            ).prefetch_related('posts'),
            serializer_class=UsersSerializer3,
        ),
        name='complex-queries-1',
    ),

    # select where the user first name starts with Mr
    # and the email dose not end with @hotmail

    path(
        'complex-queries-2',
        ListAPIView.as_view(
            queryset=User.objects.filter(
                Q(first_name__startswith='Rowadz') |
                ~Q(email__endswith='@hotmail.com')
            ).prefetch_related('posts'),
            serializer_class=UsersSerializer3,
        ),
        name='complex-queries-2',
    ),

    path(
        'complex-queries-3',
        ListAPIView.as_view(
            queryset=User.objects.annotate(lower_first_name=Lower('first_name')).filter(
                lower_first_name__startswith='Ro'.lower()
            ).prefetch_related('posts'),
            serializer_class=UsersSerializer3,
        ),
        name='complex-queries-3',
    ),

    path(
        'complex-queries-4',
        ListAPIView.as_view(
            queryset=User.objects.prefetch_related('posts__categories')
            .annotate(
                lower_first_name=Lower('first_name'),
                last_name_lower=Lower('last_name'),
            ).filter(
                Q(lower_first_name__startswith='Ro'.lower())
                | Q(last_name_lower__contains='Mo'.lower()),
                posts__categories__name__in=[
                    CategoryNames.CPP, CategoryNames.JAVASCRIPT
                ]
            ),
            serializer_class=UsersSerializer3,
        ),
        name='complex-queries-4',
    ),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import ListAPIView
from .views import LoginView, RegisterView
from .models import User
from .serializers import UsersSerializer

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        'queries/',
        ListAPIView.as_view(
            queryset=User.objects.all().prefetch_related('posts__categories'),
            serializer_class=UsersSerializer,
        ),
        name='queries'
    ),
]

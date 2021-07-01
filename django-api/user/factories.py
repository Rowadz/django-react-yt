import random
from factory.django import DjangoModelFactory
from factory.faker import Faker
from post.factories import PostFactory
from factory import (
    Sequence,
    sequence,
    RelatedFactory,
    RelatedFactoryList,
    PostGenerationMethodCall,
)
from .models import User


class UserFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    # username = Sequence(lambda n: f'User-{n}')
    password = PostGenerationMethodCall('set_password', 'secret')
    # posts = RelatedFactory(PostFactory, 'user')
    posts = RelatedFactoryList(
        PostFactory, 'user', size=lambda: random.randint(1, 5))

    @sequence
    def username(n):
        try:
            max_id = User.objects.latest('id').id
            return f'User-{max_id + 1}'
        except User.DoesNotExist:
            return f'User-0'

    class Meta:
        model = 'user.User'
        django_get_or_create = ['username']

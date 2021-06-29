
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence, PostGenerationMethodCall, sequence
from .models import User


class UserFactory(DjangoModelFactory):
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('email')
    # username = Sequence(lambda n: f'User-{n}')
    password = PostGenerationMethodCall('set_password', 'secret')

    @sequence
    def username(n):
        max_id = User.objects.latest('id').id
        return f'User-{max_id + 1}'

    class Meta:
        model = 'user.User'
        django_get_or_create = ['username']

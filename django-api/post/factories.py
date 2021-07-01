
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import SubFactory
# from user.factories import UserFactory


class PostFactory(DjangoModelFactory):
    body = Faker('paragraph')
    # user = SubFactory(UserFactory)
    user = SubFactory('user.factories.UserFactory')

    class Meta:
        model = 'post.Post'

import random

from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import fuzzy
from factory import SubFactory, RelatedFactoryList
from .model_enums import Weight
# from user.factories import UserFactory


class CategoryPostFactory(DjangoModelFactory):
    post = SubFactory('post.factories.PostFactory')
    weight = fuzzy.FuzzyChoice(Weight)
    category = SubFactory('category.factories.CategoryFactory')

    class Meta:
        model = 'post.CategoryPost'
        # because the category is selected randomly
        django_get_or_create = ['category', 'post']


class PostFactory(DjangoModelFactory):
    body = Faker('paragraph')
    # user = SubFactory(UserFactory)
    user = SubFactory('user.factories.UserFactory')

    categories = RelatedFactoryList(
        CategoryPostFactory,
        factory_related_name='post',
        size=lambda: random.randint(1, 5),
    )

    class Meta:
        model = 'post.Post'

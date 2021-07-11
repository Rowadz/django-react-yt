from django.core.management.base import BaseCommand, CommandError
from halo import Halo
from user.factories import UserFactory
from category.factories import CategoryFactory
from category.model_enums import CategoryNames
from post.factories import CategoryPostFactory
# from post.factories import PostFactory


class Command(BaseCommand):
    help = 'Generate fake data and seed the models with them, default are 10'

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html#the-add-argument-method
        # Optional!
        parser.add_argument('--amount', type=int,
                            help='The amount of fake data you want')
        # parser.add_argument('amount', nargs='+', type=int)

    def _generate_users(self, amount):
        for key, value in CategoryNames.choices:
            CategoryFactory.create(name=key)
        # CategoryFactory.create_batch(len(CategoryNames.choices))
        UserFactory.create_batch(amount)
        # CategoryPostFactory.create_batch(amount)
        # PostFactory.create_batch(amount)

    @Halo(text='Generating...', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):
        amount = options.get('amount') or 10
        self._generate_users(amount)

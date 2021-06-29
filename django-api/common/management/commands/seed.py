from django.core.management.base import BaseCommand, CommandError
from halo import Halo
from user.factories import UserFactory


class Command(BaseCommand):
    help = 'Generate fake data and seed the models with them, default are 10'

    def add_arguments(self, parser):
        # https://docs.python.org/3/library/argparse.html#the-add-argument-method
        # Optional!
        parser.add_argument('--amount', type=int,
                            help='The amount of fake data you want')
        # parser.add_argument('amount', nargs='+', type=int)

    def _generate_users(self, amount):
        for _ in range(amount):
            UserFactory()

    @Halo(text='Generating...', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):
        amount = options.get('amount', 10)
        self._generate_users(amount)

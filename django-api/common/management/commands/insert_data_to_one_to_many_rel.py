from django.core.management.base import BaseCommand
from halo import Halo
from faker import Faker
from user.models import User
from typing import List


class Command(BaseCommand):
    help = 'Inserting data into one to many'
    faker = Faker()

    def _create_user_and_insert_posts(self):
        """
            create a user and save it then inserts many posts for the created user
        """

        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.faker.email()

        user: User = User.objects.create(
            username=f'{first_name} {last_name}',
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(f'{last_name}{email}')

        user.save()

        self._create_posts(u=user)

    def _create_posts(self, u: User):
        from post.models import Post
        posts = [
            Post(body=self.faker.paragraph(), user_id=u.id) for _ in range(10)
        ]

        posts_from_db = Post.objects.bulk_create(posts)

        print([p.id for p in posts_from_db])

    # @Halo(text='Inserting data into one to many', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):
        self._create_user_and_insert_posts()

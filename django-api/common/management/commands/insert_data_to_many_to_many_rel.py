from django.core.management.base import BaseCommand
from halo import Halo
from faker import Faker
from user.models import User
from django.db import transaction
from typing import List
from post.models import Post


class Command(BaseCommand):
    help = 'Inserting data into many to many'
    faker = Faker()

    def _create_user_and_insert_posts(self):
        """
            create a user and save it then inserts many posts for the created user
            and for reach post we need to create many categories
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
        from post.models import Post, CategoryPost

        for _ in range(1):
            p: Post = Post.objects.create(
                body='ROWADZ',
                user_id=u.id,
            )

            categories_id = [63, 69]
            raise KeyError

            data = [
                CategoryPost(post_id=p.id, category_id=c_id) for c_id in categories_id
            ]

            CategoryPost.objects.bulk_create(data)

    # @Halo(text='Inserting data into one to many', spinner='dots', color='blue', text_color='blue')

    @transaction.atomic
    def handle(self, *args, **options):
        self._create_user_and_insert_posts()

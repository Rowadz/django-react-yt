from django.core.management.base import BaseCommand
from post.models import Post


class Command(BaseCommand):
    help = 'Testing if the soft delete with the query manager works'

    # @Halo(text='running query...', spinner='dots', color='blue', text_color='blue')
    def handle(self, *args, **options):
        # qs = Post.objects.filter(is_deleted=True)
        qs = Post.all_objects.filter()
        print(qs.query)

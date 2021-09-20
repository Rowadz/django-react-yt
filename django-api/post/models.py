from django.db import models
from common.models import BaseModel, SoftDeleteModel
from user.models import User
from category.models import Category
from .model_enums import Weight


class Post(BaseModel, SoftDeleteModel):
    body = models.TextField(null=False)
    user = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(Category, through='CategoryPost')


# https://docs.djangoproject.com/en/3.2/ref/models/fields/
class CategoryPost(BaseModel):
    weight = models.CharField(
        max_length=20,
        null=False,
        choices=Weight.choices,
        default=Weight.KINDA_RELATES,
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post_id', 'category_id']]

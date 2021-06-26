from django.db import models
from common.models import BaseModel
from .model_enums import Weight
from category.models import Category
from post.models import Post


class CategoryPost(BaseModel):
    weight = models.CharField(
        max_length=20,
        null=False,
        choices=Weight.choices,
        default=Weight.KINDA_RELATES,
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

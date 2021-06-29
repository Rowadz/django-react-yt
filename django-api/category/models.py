from django.db import models
from common.models import BaseModel
from .model_enums import CategoryNames


class Category(BaseModel):

    name = models.CharField(
        max_length=20,
        null=False,
        choices=CategoryNames.choices,
        default=CategoryNames.GENERAL,
        unique=True,
    )

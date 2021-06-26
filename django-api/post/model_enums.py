from django.db import models


class Weight(models.TextChoices):
    IMPORTANT = 'IMPORTANT'
    LITTLE = 'LITTLE'
    KINDA_RELATES = 'KINDA_RELATES'

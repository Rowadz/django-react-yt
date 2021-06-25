from django.db import models
from common.models import BaseModel
from user.models import User


class Post(BaseModel):
    body = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

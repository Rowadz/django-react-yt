from django.db import models


class CategoryNames(models.TextChoices):
    GENERAL = 'GENERAL'
    JAVASCRIPT = 'JAVASCRIPT'
    PYTHON = 'PYTHON'
    RUBY = 'RUBY'
    CPP = 'CPP'
    CSHARP = 'CSHARP'
    PHP = 'PHP'

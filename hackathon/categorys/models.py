from django.db import models


class Category(models.Model):
    # カテゴリー名
    name = models.CharField(max_length=64)

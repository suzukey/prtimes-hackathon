from django.db import models


class Company(models.Model):
    # 企業ID
    company_id = models.IntegerField()
    # 企業名
    company_name = models.CharField(max_length=128)
    # 企業URL
    url = models.URLField(null=True)
    # 本社所在地
    address = models.CharField(max_length=128, null=True)
    # 業種
    industry = models.CharField(max_length=64, null=True)

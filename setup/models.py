from django.db import models

# Create your models here.
class TestModel(models.Model):
    test_value = models.CharField(max_length=512)
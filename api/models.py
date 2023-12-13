from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_url = models.ImageField

    def __str__(self):
        return self.name

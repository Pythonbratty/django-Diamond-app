from django.db import models

# Create your models here.
class Health(models.Model):
    color = models.CharField(max_length=60)
    cut = models.CharField(max_length=60)
    clarity = models.SlugField(max_length=60)
    caratWeight = models.FloatField(max_length=60)
    def __str__(self):
        return self.color

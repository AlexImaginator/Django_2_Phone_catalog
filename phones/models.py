from django.db import models


class Phone(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(default=None)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=50)

from django.db import models
from django.conf import settings

# Create your models here.
class Csvs(models.Model):
    filename = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)


class egg_monthly_price(models.Model):
    market = models.CharField(max_length=100)
    arrival_date = models.DateField()
    price = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

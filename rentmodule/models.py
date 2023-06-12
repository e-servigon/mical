from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_year = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(default = timezone.now, blank=True, null=True)
  
    def __str__ (self):
        return 'auto : %s %s %s' % (self.car_brand, self.car_model, self.car_color)

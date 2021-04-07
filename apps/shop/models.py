from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Shop(models.Model):

  shopName = models.CharField(max_length=255, blank=True, null=True,)
  user = models.OneToOneField(User, related_name='shop',blank=True, null=True, on_delete=models.CASCADE)
  registrarName = models.CharField(max_length=255, blank=True, null=True)
  registrarContact = models.CharField(max_length=255, blank=True, null=True)
  registrarAddress = models.TextField(blank=True, null=True)

  class Meta:
    verbose_name_plural='Shop'
    
  def __str__(self):
    return self.shopName


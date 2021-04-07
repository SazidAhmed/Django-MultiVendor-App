from django.db import models
from django.contrib.auth.models import User


class UserRole(models.Model):
  name = models.CharField(max_length=20)
  permissions = models.JSONField()
  def __str__(self):
    return self.name


class UserProfile(models.Model):
  BUYER='buyer'
  SELLER = 'seller'

  CHOICES_PLANS = (
    (BUYER, 'buyer'),
    (SELLER, 'seller')
  )

  user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
  plan = models.CharField(max_length=20, choices=CHOICES_PLANS, default=BUYER)
  user_role = models.ForeignKey(UserRole, related_name="userprofile", blank=True, null=True, on_delete=models.CASCADE)
  def __str__(self):
    return self.user.email
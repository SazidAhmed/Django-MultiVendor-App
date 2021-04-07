from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # Shop apis
  path('createShop', views.createShop, name="createShop"),
]
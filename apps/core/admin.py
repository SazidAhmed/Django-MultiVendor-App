from django.contrib import admin

from .models import UserProfile, UserRole

admin.site.register(UserRole)
admin.site.register(UserProfile)

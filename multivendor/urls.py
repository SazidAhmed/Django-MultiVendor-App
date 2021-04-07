from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.core.views import home

urlpatterns = [
    # Website Urls
    path('', home, name='homepage'),

    # Super Admin Panel Urls
    path('admin/', admin.site.urls),

    # djoser auth
    path('auth/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    # Api Urls
    path('authApis/', include('apps.core.urls')),
    path('itemApis/', include('apps.item.urls')),
    path('shopApis/', include('apps.shop.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

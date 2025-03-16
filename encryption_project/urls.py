"""
URL configuration for encryption_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from encryption_app.views import home_view   # ✅ Use the correct app name
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # ✅ Admin Panel
    path('admin/', admin.site.urls),

    # ✅ Home Page
    path('', home_view, name="home"),

    # ✅ Encryption App URLs
    path('', include('encryption_app.urls')),

    # ✅ Custom Authentication System
    path('auth/', include('authentication.urls')),

    # ✅ Default Django Authentication URLs (Login, Logout, Password Reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # ✅ django-allauth for Social Login (Google, Facebook, etc.)
    #path('accounts/', include('allauth.urls')),
    path("auth/", include("allauth.urls")),

]
# ✅ Serve Static & Media Files in Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

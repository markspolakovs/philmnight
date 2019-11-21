"""hacksoc_filmnight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from film_management import views as fm_views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('discord/', include('discord_auth.urls')),
    path('film_management/', include('film_management.urls')),
    path('dashboard/', fm_views.dashboard),
    path('films/', fm_views.films)
]

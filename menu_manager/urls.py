"""menu_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('starters/', include('starters.urls')),
    path('starter_dishes/', include('starter_dishes.urls')),
    path('main_courses/', include('main_courses.urls')),
    path('main_course_dishes/', include('main_dishes.urls')),
    path('sides/', include('sides.urls')),
    path('sauces/', include('sauces.urls')),
    path('desserts/', include('desserts.urls')),
    path('dessert_sauces/', include('dessert_sauces.urls')),
    path('dessert_dishes/', include('dessert_dishes.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('accounts/', include('allauth.urls')),
    ]

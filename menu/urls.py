from django.urls import path
from .views import ViewMenus
from . import views


urlpatterns = [
    path("",ViewMenus.as_view(),name="menus"),
         ]
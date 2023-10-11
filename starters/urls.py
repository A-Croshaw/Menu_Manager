from django.urls import path
from .views import ViewStarter


urlpatterns = [
    path("",
         ViewStarter.as_view(),
         name="starters"
         ),]


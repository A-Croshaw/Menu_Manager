from django.urls import path
from .views import ViewMenus
from . import views


urlpatterns = [
    path("",ViewMenus.as_view(),name="menus"),
    path('menu/add_menu/',views.add_menu,name='add_menu'),
    path('menu_view/<pk>/',views.menu_view,name='menu_view'),
    path('add_starter_item/<pk>/',views.add_starter_item,name='add_starter_item'),
    path('htmx/add_starter/',views.add_starter,name='add_starter'),
    path('htmx/menu_starter_details/<pk>/',views.menu_starter_details,name="menu_starter_details"),
    path('htmx/menu_starter_view/<pk>/',views.menu_starter_details,name="menu_starter_view"),
    path('add_main_item/<pk>/',views.add_main_item,name='add_main_item'),
    path('htmx/add_main/',views.add_main,name='add_main'),
    path('htmx/menu_main_details/<pk>/',views.menu_main_details,name="menu_main_details"),
    path('htmx/menu_main_view/<pk>/',views.menu_main_view,name="menu_main_view"),
    path('add_dessert_item/<pk>/',views.add_dessert_item,name='add_dessert_item'),
    path('htmx/add_dessert/',views.add_dessert,name='add_dessert'),
    path('htmx/menu_dessert_details/<pk>/',views.menu_dessert_details,name="menu_dessert_details"),
    path('htmx/menu_dessert_view/<pk>/',views.menu_dessert_view,name="menu_dessert_view"),
]
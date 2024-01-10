from django.urls import path
from .views import ViewMenus
from . import views


urlpatterns = [
    path("",ViewMenus.as_view(),name="menus"),
    path('menu/add_menu/',views.add_menu,name='add_menu'),
    path('menu_view/<pk>/',views.menu_view,name='menu_view'),
    # starters
    path('add_starter_item/<pk>/',views.add_starter_item,name='add_starter_item'),
    path('htmx/add_starter/',views.add_starter,name='add_starter'),
    path('htmx/menu_starter_details/<pk>/',views.menu_starter_details,name="menu_starter_details"),
    path('htmx/menu_starter_view/<pk>/',views.menu_starter_details,name="menu_starter_view"),
    # mains
    path('add_main_item/<pk>/',views.add_main_item,name='add_main_item'),
    path('htmx/add_main/',views.add_main,name='add_main'),
    path('htmx/menu_main_details/<pk>/',views.menu_main_details,name="menu_main_details"),
    path('htmx/menu_main_view/<pk>/',views.menu_main_view,name="menu_main_view"),
    # desserts
    path('add_dessert_item/<pk>/',views.add_dessert_item,name='add_dessert_item'),
    path('htmx/add_dessert/',views.add_dessert,name='add_dessert'),
    path('htmx/menu_dessert_details/<pk>/',views.menu_dessert_details,name="menu_dessert_details"),
    path('htmx/menu_dessert_view/<pk>/',views.menu_dessert_view,name="menu_dessert_view"),
    # sides
    path('add_side_item/<pk>/',views.add_side_item,name='add_side_item'),
    path('htmx/add_side/',views.add_side,name='add_side'),
    path('htmx/menu_side_details/<pk>/',views.menu_side_details,name="menu_side_details"),
    path('htmx/menu_side_view/<pk>/',views.menu_side_view,name="menu_side_view"),
    # sauces
    path('add_sauce_item/<pk>/',views.add_sauce_item,name='add_sauce_item'),
    path('htmx/add_sauce/',views.add_sauce,name='add_sauce'),
    path('htmx/menu_sauce_details/<pk>/',views.menu_sauce_details,name="menu_sauce_details"),
    path('htmx/menu_sauce_view/<pk>/',views.menu_sauce_view,name="menu_sauce_view"),
]
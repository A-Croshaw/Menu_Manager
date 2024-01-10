from django.urls import path
from .views import ViewMenus, MenuDelete
from . import views


urlpatterns = [
    path("",ViewMenus.as_view(),name="menus"),
    path('menu/add_menu/',views.add_menu,name='add_menu'),
    path('menu_view/<pk>/',views.menu_view,name='menu_view'),
    path('edit_menu/<pk>/update/',views.edit_menu,name="edit_menu"),
    path('menu_delete/<pk>/delete/',MenuDelete.as_view(),name="menu_delete"),
    # starters
    path('add_starter_item/<pk>/',views.add_starter_item,name='add_starter_item'),
    path('htmx/add_starter/',views.add_starter,name='add_starter'),
    path('htmx/menu_starter_details/<pk>/',views.menu_starter_details,name="menu_starter_details"),
    path('htmx/menu_starter_view/<pk>/',views.menu_starter_details,name="menu_starter_view"),
    path('htmx/edit_menu_starter/<pk>/update/',views.edit_menu_starter,name="edit_menu_starter"),
    path('htmx/delete_starter_dish_item/<pk>/delete/',views.delete_starter_dish_item,name="delete_starter_dish_item"),
    # mains
    path('add_main_item/<pk>/',views.add_main_item,name='add_main_item'),
    path('htmx/add_main/',views.add_main,name='add_main'),
    path('htmx/menu_main_details/<pk>/',views.menu_main_details,name="menu_main_details"),
    path('htmx/menu_main_view/<pk>/',views.menu_main_view,name="menu_main_view"),
    path('htmx/edit_menu_main/<pk>/update/',views.edit_menu_main,name="edit_menu_main"),
    path('htmx/delete_main_dish_item/<pk>/delete/',views.delete_main_dish_item,name="delete_main_dish_item"),
    # desserts
    path('add_dessert_item/<pk>/',views.add_dessert_item,name='add_dessert_item'),
    path('htmx/add_dessert/',views.add_dessert,name='add_dessert'),
    path('htmx/menu_dessert_details/<pk>/',views.menu_dessert_details,name="menu_dessert_details"),
    path('htmx/menu_dessert_view/<pk>/',views.menu_dessert_view,name="menu_dessert_view"),
    path('htmx/edit_menu_dessert/<pk>/update/',views.edit_menu_dessert,name="edit_menu_dessert"),
    path('htmx/delete_dessert_dish_item/<pk>/delete/',views.delete_dessert_dish_item,name="delete_dessert_dish_item"),
    # sides
    path('add_side_item/<pk>/',views.add_side_item,name='add_side_item'),
    path('htmx/add_side/',views.add_side,name='add_side'),
    path('htmx/menu_side_details/<pk>/',views.menu_side_details,name="menu_side_details"),
    path('htmx/menu_side_view/<pk>/',views.menu_side_view,name="menu_side_view"),
    path('htmx/edit_menu_side/<pk>/update/',views.edit_menu_side,name="edit_menu_side"),
    path('htmx/delete_side_item/<pk>/delete/',views.delete_side_item,name="delete_side_item"),
    # sauces
    path('add_sauce_item/<pk>/',views.add_sauce_item,name='add_sauce_item'),
    path('htmx/add_sauce/',views.add_sauce,name='add_sauce'),
    path('htmx/menu_sauce_details/<pk>/',views.menu_sauce_details,name="menu_sauce_details"),
    path('htmx/menu_sauce_view/<pk>/',views.menu_sauce_view,name="menu_sauce_view"),
    path('htmx/edit_menu_sauce/<pk>/update/',views.edit_menu_sauce,name="edit_menu_sauce"),
    path('htmx/delete_sauce_item/<pk>/delete/',views.delete_sauce_item,name="delete_sauce_item"),
]
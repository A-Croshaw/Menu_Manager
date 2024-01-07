from django.urls import path
from .views import ViewMainDish, MainDishDelete
from . import views


urlpatterns = [
     path("",ViewMainDish.as_view(),name="main_dishes"),
     path('main_dishes/add_main_dish/',views.add_main_dish,name='add_main_dish'),
     path('main_dish_view/<pk>/',views.main_dish_view,name='main_dish_view'),
     path('edit_main_dish/<pk>/update/',views.edit_main_dish,name="edit_main_dish"),
     path('main_dish_delete/<pk>/delete/',MainDishDelete.as_view(),name="main_dish_delete"),
     path('main_dish_element/<pk>/',views.main_dish_element,name='main_dish_element'),
     path('htmx/add_main_dish_element/',views.add_main_dish_element,name='add_main_dish_element'),
     path('htmx/main_dish_element_details/<pk>/update/',views.main_dish_element_details,name="main_dish_element_details"),
     path('htmx/update_main_dish_element/<pk>/update/',views.update_main_dish_element,name="update_main_dish_element"),
     path('htmx/delete_main_dish_element/<pk>/delete/',views.delete_main_dish_element,name="delete_main_dish_element"),
     path('main_dish_sauce/<pk>/',views.main_dish_sauce,name='main_dish_sauce'),
     path('htmx/add_main_dish_sauce/',views.add_main_dish_sauce,name='add_main_dish_sauce'),
     path('htmx/main_dish_sauce_details/<pk>/update/',views.main_dish_sauce_details,name="main_dish_sauce_details"),
     path('htmx/update_main_dish_sauce/<pk>/update/',views.update_main_dish_sauce,name="update_main_dish_sauce"),
     path('htmx/delete_main_dish_sauce/<pk>/delete/',views.delete_main_dish_sauce,name="delete_main_dish_sauce"),
]
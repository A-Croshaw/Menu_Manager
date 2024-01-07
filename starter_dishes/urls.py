from django.urls import path
from .views import ViewStarterDish, StarterDishDelete
from . import views


urlpatterns = [
     path("",ViewStarterDish.as_view(),name="starter_dishes"),
     path('starter_dishes/add_starter_dish/',views.add_starter_dish,name='add_starter_dish'),
     path('starter_dish_view/<pk>/',views.starter_dish_view,name='starter_dish_view'),
     path('edit_starter_dish/<pk>/update/',views.edit_starter_dish,name="edit_starter_dish"),
     path('starter_dish_delete/<pk>/delete/',StarterDishDelete.as_view(),name="starter_dish_delete"),
     path('starter_dish_element/<pk>/',views.starter_dish_element,name='starter_dish_element'),
     path('htmx/add_starter_dish_element/',views.add_starter_dish_element,name='add_starter_dish_element'),
     path('htmx/starter_dish_element_details/<pk>/update/',views.starter_dish_element_details,name="starter_dish_element_details"),
     path('htmx/update_starter_dish_element/<pk>/update/',views.update_starter_dish_element,name="update_starter_dish_element"),
     path('htmx/delete_starter_dish_element/<pk>/delete/',views.delete_starter_dish_element,name="delete_starter_dish_element"),
     path('starter_dish_sauce/<pk>/',views.starter_dish_sauce,name='starter_dish_sauce'),
     path('htmx/add_starter_dish_sauce/',views.add_starter_dish_sauce,name='add_starter_dish_sauce'),
     path('htmx/starter_dish_sauce_details/<pk>/update/',views.starter_dish_sauce_details,name="starter_dish_sauce_details"),
     path('htmx/update_starter_dish_sauce/<pk>/update/',views.update_starter_dish_sauce,name="update_starter_dish_sauce"),
     path('htmx/delete_starter_dish_sauce/<pk>/delete/',views.delete_starter_dish_sauce,name="delete_starter_dish_sauce"),
]
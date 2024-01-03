from django.urls import path
from .views import ViewDessertDish, DessertDishDelete
from . import views


urlpatterns = [
     path("",ViewDessertDish.as_view(),name="dessert_dishes"),
     path('dessert_dishes/add_dessert_dish/',views.add_dessert_dish,name='add_dessert_dish'),
     path('dessert_dish_view/<pk>/',views.dessert_dish_view,name='dessert_dish_view'),
     path('edit_dessert_dish/<pk>/update/',views.edit_dessert_dish,name="edit_dessert_dish"),
     path('dessert_dish_delete/<pk>/delete/',DessertDishDelete.as_view(),name="dessert_dish_delete"),
     path('dessert_dish_element/<pk>/',views.dessert_dish_element,name='dessert_dish_element'),
     path('htmx/add_dessert_dish_element/',views.add_dessert_dish_element,name='add_dessert_dish_element'),
     path('htmx/dessert_dish_element_details/<pk>/update/',views.dessert_dish_element_details,name="dessert_dish_element_details"),
     path('htmx/update_dessert_dish_element/<pk>/update/',views.update_dessert_dish_element,name="update_dessert_dish_element"),
     path('htmx/delete_dessert_dish_element/<pk>/delete/',views.delete_dessert_dish_element,name="delete_dessert_dish_element"),
     path('dessert_dish_sauce/<pk>/',views.dessert_dish_sauce,name='dessert_dish_sauce'),
     path('htmx/add_dessert_dish_sauce/',views.add_dessert_dish_sauce,name='add_dessert_dish_sauce'),
     path('htmx/dessert_dish_sauce_details/<pk>/update/',views.dessert_dish_sauce_details,name="dessert_dish_sauce_details"),
     path('htmx/update_dessert_dish_sauce/<pk>/update/',views.update_dessert_dish_sauce,name="update_dessert_dish_sauce"),
     path('htmx/delete_dessert_dish_sauce/<pk>/delete/',views.delete_dessert_dish_sauce,name="delete_dessert_dish_sauce"),
]
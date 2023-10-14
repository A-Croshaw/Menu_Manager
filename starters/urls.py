from django.urls import path
from .views import ViewStarter, StarterDelete
from . import views


urlpatterns = [
    path("",
         ViewStarter.as_view(),
         name="starters"
         ),
    path('starter/add_starter/',
         views.add_starter,
         name='add_starter'
         ),
    path('starter_view/<pk>/',
         views.starter_view,
         name='starter_view'
         ),
    path('edit_starter/<pk>/update/',
         views.edit_starter,
         name="edit_starter"
         ),
    path('starter_delete/<pk>/delete/',
         StarterDelete.as_view(),
         name="starter_delete"
         ),
    path('starter_method/<pk>/',
         views.starter_method,
         name='starter_method'
         ),
    path('starter_ingredients/<pk>/',
         views.starter_ingredients,
         name='starter_ingredients'
         ),
    path('htmx/add_starter_ing/',
         views.add_starter_ing,
         name='add_starter_ing'
         ),
    path('htmx/starter_ing_details/<pk>/',
         views.starter_ing_details,
         name="starter_ing_details"
         ),
    path('starter_ing_detail_view/<pk>/',
         views.starter_ing_detail_view,
         name="starter_ing_detail_view"
         ),
    path('starter_step_detail_view/<pk>/',
         views.starter_step_detail_view,
         name="starter_step_detail_view"
         ),
    path('htmx/update_starter_ing/<pk>/update/',
         views.update_starter_ing,
         name="update_starter_ing"
         ),
    path('htmx/delete_ingredient/<pk>/delete/',
         views.delete_starter_ing,
         name="delete_starter_ing"
         ),
    path('htmx/add_starter_step/',
         views.add_starter_step,
         name='add_starter_step'
         ),
    path('htmx/starter_step_details/<pk>/update/',
         views.starter_step_details,
         name="starter_step_details"
         ),
    path('htmx/update_starter_step/<pk>/update/',
         views.update_starter_step,
         name="update_starter_step"
         ),
    path('htmx/delete_starter_step/<pk>/delete/',
         views.delete_starter_step,
         name="delete_starter_step"
         ),
]

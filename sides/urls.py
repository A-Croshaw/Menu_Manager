from django.urls import path
from .views import ViewSide, SideDelete
from . import views


urlpatterns = [
    path("",
         ViewSide.as_view(),
         name="sides"
         ),
    path('side/add_side/',
         views.add_side,
         name='add_side'
         ),
    path('side_view/<pk>/',
         views.side_view,
         name='side_view'
         ),
    path('edit_side/<pk>/update/',
         views.edit_side,
         name="edit_side"
         ),
    path('side_delete/<pk>/delete/',
         SideDelete.as_view(),
         name="side_delete"
         ),
    path('side_method/<pk>/',
         views.side_method,
         name='side_method'
         ),
    path('side_ingredients/<pk>/',
         views.side_ingredients,
         name='side_ingredients'
         ),
    path('htmx/add_side_ing/',
         views.add_side_ing,
         name='add_side_ing'
         ),
    path('htmx/side_ing_details/<pk>/',
         views.side_ing_details,
         name="side_ing_details"
         ),
    path('side_ing_detail_view/<pk>/',
         views.side_ing_detail_view,
         name="side_ing_detail_view"
         ),
    path('side_step_detail_view/<pk>/',
         views.side_step_detail_view,
         name="side_step_detail_view"
         ),
    path('htmx/update_side_ing/<pk>/update/',
         views.update_side_ing,
         name="update_side_ing"
         ),
    path('htmx/delete_ingredient/<pk>/delete/',
         views.delete_side_ing,
         name="delete_side_ing"
         ),
    path('htmx/add_side_step/',
         views.add_side_step,
         name='add_side_step'
         ),
    path('htmx/side_step_details/<pk>/update/',
         views.side_step_details,
         name="side_step_details"
         ),
    path('htmx/update_side_step/<pk>/update/',
         views.update_side_step,
         name="update_side_step"
         ),
    path('htmx/delete_side_step/<pk>/delete/',
         views.delete_side_step,
         name="delete_side_step"
         ),
]

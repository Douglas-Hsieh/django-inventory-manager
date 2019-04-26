from django.urls import path
from inventory_manager.views import home_view,\
    drink_create_view, drink_detail_view, drink_update_view, drink_delete_view, drink_list_view,\
    snack_create_view, snack_detail_view, snack_update_view, snack_delete_view, snack_list_view

app_name = 'inventory_manager'

urlpatterns = [
    path('', home_view, name='home'),

    path('drink_create/', drink_create_view, name='drink_create'),
    path('<int:pk>/drink_detail/', drink_detail_view, name='drink_detail'),
    path('<int:pk>/drink_update/', drink_update_view, name='drink_update'),
    path('<int:pk>/drink_delete/', drink_delete_view, name='drink_delete'),
    path('drink_list/', drink_list_view, name='drink_list'),

    path('snack_create/', snack_create_view, name='snack_create'),
    path('<int:pk>/snack_detail/', snack_detail_view, name='snack_detail'),
    path('<int:pk>/snack_update/', snack_update_view, name='snack_update'),
    path('<int:pk>/snack_delete/', snack_delete_view, name='snack_delete'),
    path('snack_list/', snack_list_view, name='snack_list'),
]

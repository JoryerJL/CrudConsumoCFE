from django.urls import path
from .views import ClientListView, ClientCreateView, add_state, add_postal_code, add_colony, add_municipality

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('add_state/', add_state, name='add_state'),
    path('add_postal_code/', add_postal_code, name='add_postal_code'),
    path('add_colony/', add_colony, name='add_colony'),
    path('add_municipality/', add_municipality, name='add_municipality'),
]

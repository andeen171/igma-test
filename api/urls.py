from django.urls import path
from api.views import client_detail, client_list, ClientViewSet

urlpatterns = [
    # Function Views
    path('clients/', client_list),
    path('clients/<int:pk>/', client_detail),
    # Viewset
    path('clientes/', ClientViewSet.as_view({'get': 'list', 'post': 'create'}), name='clientes'),
    path('clientes/<int:cpf>/', ClientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='cliente'),
]

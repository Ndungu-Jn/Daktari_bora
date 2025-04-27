from django.urls import path
from .api_views import (
    ClientListCreate, 
    ClientRetrieveUpdateDestroy, 
    ClientProgramListCreate,
    ClientProgramRetrieveUpdateDestroy
)

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='api_client_list_create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroy.as_view(), name='api_client_detail'),
    path('clients/<int:client_id>/programs/', ClientProgramListCreate.as_view(), name='api_client_program_list_create'),
    path('clients/<int:client_id>/programs/<int:pk>/', ClientProgramRetrieveUpdateDestroy.as_view(), name='api_client_program_detail'),
]
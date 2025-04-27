from django.urls import path
from .api_views import ProgramListCreate, ProgramRetrieveUpdateDestroy

urlpatterns = [
    path('', ProgramListCreate.as_view(), name='api_program_list_create'),
    path('<int:pk>/', ProgramRetrieveUpdateDestroy.as_view(), name='api_program_detail'),
]
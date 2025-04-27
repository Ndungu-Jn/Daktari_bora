from django.urls import path
from . import views

urlpatterns = [
    path('', views.program_list, name='program_list'),
    path('<int:pk>/', views.program_detail, name='program_detail'),
    path('create/', views.program_create, name='program_create'),
    path('<int:pk>/update/', views.program_update, name='program_update'),
]
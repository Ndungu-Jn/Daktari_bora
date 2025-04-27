from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/clients/', permanent=True)),
    path('clients/', include('clients.urls')),
    path('programs/', include('programs.urls')),
    path('api/', include('clients.api_urls')),
    path('api/programs/', include('programs.api_urls')),
    
    # Use only this for all auth URLs (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
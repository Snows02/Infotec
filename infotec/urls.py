from django.contrib import admin
from django.urls import include, path
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/', include('management.urls')),
    path('users/', include('users.urls')),
    path('', landing, name='landing'),
    path('loginsis', loginsis, name='login'),
    path('logout', cerrarSesion, name='logout'),
]

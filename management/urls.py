from django.urls import path
from management.views import *

urlpatterns = [
    path('menu', menu, name='menu'),
    path('diagnostico', gotodiagnostico, name='diagnostico'),
]

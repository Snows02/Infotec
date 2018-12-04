from django.contrib import admin
from django.urls import include, path
from users.views import *


urlpatterns = [
	path('register', register, name='register'),
]
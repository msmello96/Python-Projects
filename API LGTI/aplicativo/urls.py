from django.urls import include, path
from . import views

urlpatterns = [
    path('app/', views.home, name='home')
]
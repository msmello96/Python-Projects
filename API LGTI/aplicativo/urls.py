from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.alteracao, name='alteracao'),
    path('sair/', views.sair, name="sair"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.atualiza_cliente, name="atualiza_cliente"),
    path('update_carro/<int:id>', views.update_carro, name="update_carro"),
    path('excluir_carro/<int:id>', views.excluir_carro, name="excluir_carro")
]
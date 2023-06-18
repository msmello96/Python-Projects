from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.pacientes, name="pacientes"),
    path('dados_paciente/', views.dados_paciente_listar, name="dados_paciente_listar"),
    path('dados_paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
    path('medidas_paciente/', views.medidas_paciente_listar, name="medidas_paciente_listar"),
    path('medidas_paciente/<str:id>/', views.medidas_paciente, name="medidas_paciente"),
    path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    path('grafico_gordura/<str:id>/', views.grafico_gordura, name="grafico_gordura"),
    path('grafico_musculo/<str:id>/', views.grafico_musculo, name="grafico_musculo"),
    path('plano_alimentar_listar/', views.plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<str:id>/', views.plano_alimentar, name="plano_alimentar"),
    path('refeicao/<str:id_paciente>/', views.refeicao, name="refeicao"),
    path('opcao/<str:id_paciente>/', views.opcao, name="opcao"),
    path('exportar_refeicao/<str:id_paciente>/', views.exportar_refeicao, name="exportar_refeicao"),
]
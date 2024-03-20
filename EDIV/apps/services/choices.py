from django.db.models import TextChoices

class BudgetStatus(TextChoices):
    SOLICITADO = 'SO', 'Orçamento Solicitado'
    EM_ANALISE = 'EA', 'Em Análise'
    REALIZADO = 'R', 'Realizado'
    CANCELADO = 'C', 'Cancelado'
    FECHADO = 'F', 'Fechado'

class ServiceTags(TextChoices):
    MOTION = 'M', 'Motion design'
    EDICAO_IMAGEM = 'EI', 'Edição de imagem'
    EDICAO_VIDEO = 'EV', 'Edição de video'
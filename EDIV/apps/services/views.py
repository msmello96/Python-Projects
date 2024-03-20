from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import TemporaryUploadedFile, InMemoryUploadedFile
from .uploaded_file import ChunkUploadedFile
from .utils import is_video
from tinymce.widgets import TinyMCE
from .choices import ServiceTags
from .models import Budget
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.utils.safestring import mark_safe

def request_budget(request):
    if request.method == 'GET':
        HTML_FIELD = TinyMCE().render(name='descricao', value='', attrs={'id': 'id_descricao'})
        return render(request, 'request_budget.html', {'HTML_FIELD': HTML_FIELD, 'services': ServiceTags.choices})
    elif request.method == 'POST':
        file = request.FILES.get('file')
        service = request.POST.get('service')
        descricao = request.POST.get('descricao')

        if not is_video(file):
            raise HttpResponseBadRequest()
        
        file_uploaded = ChunkUploadedFile(file)
        file_path = file_uploaded.save_disk()

        budget = Budget(
            file_path = file_path,
            data = datetime.now(),
            service_tag = service,
            descricao = descricao,
            cliente = request.user,
        )

        budget.save()

        #TODO: redirecionar para visualizacao do orcamento

        messages.add_message(request, constants.SUCCESS, mark_safe('Orcamento solicitado com sucesso. <a href="#">Clique Aqui</a> para ver o status.'))
        
        return redirect(reverse('request_budget'))
from django.test import TestCase
from views import logar

def getMidiaId(media):
    usuario = "lgti.marcelo"
    senha = "SEnhadeLogin@"
    retorno = logar(1).mediatype.get(
        filter={"name": media}
    )

    return retorno[0]["mediatypeid"]

media = "Ligação Webhook 2"
id = getMidiaId(media)
print(id)



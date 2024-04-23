from rest_framework import viewsets, filters
import json
from contatos.models import Contato, Pensamento
from contatos.serializer import ContatoSerializer, PensamentoSerializer
# from .forms import ContatoForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class ContatosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os contatos"""
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']


class PensamentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Pensamentos"""
    queryset = Pensamento.objects.all()
    serializer_class = PensamentoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['conteudo']
    filterset_fields = ['favorito']

@csrf_exempt
def contatoEmail(request):
    if request.method == 'POST':
        # Decodificar o JSON recebido
        data = json.loads(request.body)

        # Chamar o método send_email no modelo
        Contato().send_email(**data)

        # Retornar uma resposta JSON indicando sucesso
        return JsonResponse({"mensagem": "Email enviado com sucesso"})

    # Retornar uma resposta JSON indicando que algo deu errado
    return JsonResponse({"mensagem": "Erro no envio do email"}, status=400)

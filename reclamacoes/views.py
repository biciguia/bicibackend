from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from reclamacoes.models import Reclamacao 
from reclamacoes.serializers import ReclamacaoSerializer 
from pprint import pprint


class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSON.
  """
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def reclamacao_list(request):
  """
  Lista todas as reclamações em GET, cria uma nova com POST 
  """
  if request.method == "GET":
    reclamacoes = Reclamacao.objects.all()
    serializer = ReclamacaoSerializer(reclamacoes, many=True)
    return JSONResponse(serializer.data)

  elif request.method == "POST":
    data = JSONParser().parse(request)
    print("\n\n\n\n\n")
    pprint(data)
    print("\n\n\n\n\n")
    serializer = ReclamacaoSerializer(data=data)
    if serializer.is_valid():
      print("\n\n\n\n\nPelo menos é válido\n\n\n\n")
      serializer.save()
      return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

# Create your views here.

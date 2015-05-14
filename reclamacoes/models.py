#from django.db import models
#from django.contrib.gis.db.models import PointField, LineStringField
from django.contrib.gis.db import models

# Create your models here.

class Reclamacao(models.Model):
  texto = models.TextField('Texto de feedback')
  endereco_origem = models.TextField('Endereço de origem')
  endereco_destino = models.TextField('Endereço de destino')
  ponto_origem = models.PointField('Coordenada de origem')
  ponto_destino = models.PointField('Coordenada de destino')
  rota_tracada = models.LineStringField('Rota traçada pelo aplicativo')




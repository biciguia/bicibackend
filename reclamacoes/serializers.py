from django.forms import widgets
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from reclamacoes.models import Reclamacao

class ReclamacaoSerializer(GeoFeatureModelSerializer):
  class Meta:
    model = Reclamacao
    geo_field = "point" # Necessidade do rest_framework_gis
    #fields = ('texto', 'endereco_origem', 'endereco_destino', 'ponto_origem', 'ponto_destino', 'rota_tracada')

  # def create(self, validated_data):
  #         # Create the book instance
  #         return Reclamacao.objects.create(**validated_data)

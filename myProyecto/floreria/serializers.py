#que es un serializador en django
#bbdd -> datos -> JSON
#JSON -> datos -> bbdd

from rest_framework import serializers
from .models import Flor


class FlorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Flor
        fields = ['name', 'valor', 'descripcion', 'estado', 'stock', 'categoria']
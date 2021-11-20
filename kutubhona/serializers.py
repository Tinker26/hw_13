from rest_framework import serializers
from .models import *


class KitobSerializer(serializers.ModelSerializer):
    class Meta():
        model = Kitob
        fields = '__all__'

class MuallifSerializer(serializers.ModelSerializer):
    kitoblar = KitobSerializer(read_only=True, many=True)
    class Meta():
        model = Muallif
        fields = '__all__'

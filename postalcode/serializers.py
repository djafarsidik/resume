from rest_framework import serializers
from .models import Provinsi, Kab_kota

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinsi
        fields = ['code', 'nama']
        
class KabkotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kab_kota
        fields = ['code', 'nama', 'type', 'provinsi']
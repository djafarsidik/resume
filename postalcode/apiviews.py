from .models import Provinsi, Kab_kota
from rest_framework import viewsets, permissions
from .serializers import ProvinsiSerializer, KabkotaSerializer

class ProvinsiViewSets(viewsets.ModelViewSet):
    queryset = Provinsi.objects.all().order_by('nama')
    serializer_class = ProvinsiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class KabkotaViewSets(viewsets.ModelViewSet):
    queryset = Kab_kota.objects.all().order_by('nama')
    serializer_class = KabkotaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
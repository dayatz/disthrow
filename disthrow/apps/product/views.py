from rest_framework import viewsets
from apps.distro.models import Distro
from .models import Product
from .serializers import ProductSerializer


class ProductViewsSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(distro_id=self.kwargs.get('group_pk'))

    def perform_create(self, serializer):
        distro = Distro.objects.get(pk=self.kwargs.get('distro_pk'))
        serializer.save(distro=distro)

from rest_framework import viewsets
from .serializers import DistroSerializer
from .models import Distro


class DistroViewSet(viewsets.ModelViewSet):
    serializer_class = DistroSerializer
    queryset = Distro.objects.all()

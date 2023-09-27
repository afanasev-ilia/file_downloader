from rest_framework import viewsets

from api.serializers import FileSerializer
from files.models import File



class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('-uploaded_at')
    serializer_class = FileSerializer

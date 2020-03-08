#Django rest_framework
from rest_framework import mixins, viewsets
#Serializers
from publication.serializers import PublicationModelSerializer
#Models
from publication.models import Publication

class PublicationViewSet(viewsets.ModelViewSet):
    """Publication view set."""
    queryset = Publication.objects.all()
    serializer_class = PublicationModelSerializer

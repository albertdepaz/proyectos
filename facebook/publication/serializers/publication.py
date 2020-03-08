"""publication serializers."""
#Django rest_frameworks
from rest_framework import serializers
from publication.models import Publication

class PublicationModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Publication
        fields = (
            'user',
            'picture',
            'description',
            'like_taken',
        )
    

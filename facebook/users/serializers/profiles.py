"""Profile serializer."""
#Django rest_framework
from rest_framework import serializers
#Models
from users.models import Profile
class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    class Meta:
        model = Profile
        fields = (
            'picture',
            'biography',
        )

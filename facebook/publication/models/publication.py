from django.db import models

from utils.models import CRideModel

class Publication(CRideModel):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(
        'publication picture',
        upload_to='publication/pictures/',
        blank=True,
        null=True
    )
    description = models.TextField(max_length=500, blank=True)
    #Stats
    like_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)
    
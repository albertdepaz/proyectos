from django.db import models

from utils.models import CRideModel

class Comment(CRideModel):
    publication = models.ForeignKey('publication.Publication', on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(
        'comments picture',
        upload_to='comments/pictures/',
        blank=True,
        null=True
    )
    description = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return str(self.publication)
    
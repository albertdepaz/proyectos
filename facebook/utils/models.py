"""Django models utilities."""
#Django
from django.db import models

class CRideModel(models.Model):
    """comprate Ride base model."""
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on wich the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now_add=True,
        help_text='Date time on wich the object was last modified.'
    )

    class Meta:
        "meta option."
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']


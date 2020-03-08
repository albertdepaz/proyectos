from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import CRideModel
from django.core.validators import RegexValidator

class User(CRideModel, AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist.'
        }
    )
    
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
    )

    phone_number = models.CharField(validators=[phone_regex],max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField (
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clents are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='set to true when the user have verified its email address.'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        """return username"""
        return self.username
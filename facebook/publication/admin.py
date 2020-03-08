from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from publication.models import Publication
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display=('user','picture','description','like_taken')


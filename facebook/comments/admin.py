from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from comments.models import Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('publication','picture','description')

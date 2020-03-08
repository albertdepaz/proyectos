from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from users.models import User,Profile

class CustomUserAdmin(UserAdmin):
    """User model admin"""
    list_display = ('email','first_name','last_name','phone_number')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')

@admin.register(Profile)
  
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'biography')
    search_fields = ('user__username', 'user__email', 'user__first_name','user__last_name')
admin.site.register(User, CustomUserAdmin)
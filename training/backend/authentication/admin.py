from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nickname', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('username', 'email', 'nickname')

admin.site.register(CustomUser, CustomUserAdmin)

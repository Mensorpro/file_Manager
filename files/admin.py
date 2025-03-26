from django.contrib import admin
from .models import UserFile

@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'upload_date', 'file_size')
    list_filter = ('user', 'upload_date')
    search_fields = ('filename', 'user__username')
    date_hierarchy = 'upload_date'
    ordering = ('-upload_date',)

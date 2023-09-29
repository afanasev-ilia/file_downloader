from django.contrib import admin

from files.models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'uploaded_at',
        'processed',
    )
    empty_value_display = '-пусто-'

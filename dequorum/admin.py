from django.contrib import admin

from . import models

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'owner', 'is_open', 'is_visible',)
    list_filter = ('created', 'owner', 'is_open', 'is_visible',)

admin.site.register(models.Tag)
admin.site.register(models.Message)
admin.site.register(models.Thread, ThreadAdmin)

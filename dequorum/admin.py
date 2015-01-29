from django.contrib import admin

from . import models

admin.site.register(models.Tag)
admin.site.register(models.Message)
admin.site.register(models.Thread)

from django.contrib import admin
from .models import Hwmsuser

class HwmsuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(Hwmsuser, HwmsuserAdmin)
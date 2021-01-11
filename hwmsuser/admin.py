from django.contrib import admin
from .models import Hwmsuser

class HwmsuserAdmin(admin.ModelAdmin):
    list_display = ('user_sn', 'email', 'password', 'user_se', 'frst_reg_dttm')
    # list_display = ('user_sn', 'user_nm', 'email', 'password', 'user_se', 'frst_reg_dttm')

admin.site.register(Hwmsuser, HwmsuserAdmin)
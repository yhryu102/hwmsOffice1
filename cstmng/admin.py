from django.contrib import admin
from .models import CstModel

class CstmngAdmin(admin.ModelAdmin):
    list_display = ('user_sn', 'email', 'password', 'user_se', 'frst_reg_dttm')

admin.site.register(CstModel, CstmngAdmin)
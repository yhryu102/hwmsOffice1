from django.contrib import admin
from .models import Rsvmng


class RsvmngAdmin(admin.ModelAdmin):
    list_display = ('chart_no', 'cst_nm', 'rsv_branch', 'rsv_dt', 'rsv_time', 'clnic_cd', 'rsv_stt_cd')


admin.site.register(Rsvmng, RsvmngAdmin)

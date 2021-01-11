from django.contrib import admin
from .models import Rsvmng


class RsvmngAdmin(admin.ModelAdmin):
    # list_display = ('hwmsuser', 'ds_srop_desc')
    list_display = ('rsv_sn', 'rsv_dt', 'rsv_time', 'ds_srop_desc', 'ds_class', 'frst_reg_dttm')

admin.site.register(Rsvmng, RsvmngAdmin)

from django.contrib import admin
from .models import Rsvmng


class RsvmngAdmin(admin.ModelAdmin):
    # list_display = ('hwmsuser', 'goods_nm')
    list_display = ('rsv_sn', 'rsv_dt', 'rsv_time', 'goods_nm', 'ds_class', 'frst_reg_dttm')

admin.site.register(Rsvmng, RsvmngAdmin)

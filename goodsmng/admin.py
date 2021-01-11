from django.contrib import admin
from .models import GoodsModel


class GoodsmngAdmin(admin.ModelAdmin):
    list_display = ('goods_cd', 'goods_nm', 'sub_clas_nm', 'goods_at', 'goods_amt', 'tera_at', 'frst_reg_dttm')


admin.site.register(GoodsModel, GoodsmngAdmin)

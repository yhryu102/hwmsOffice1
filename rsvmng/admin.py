from django.contrib import admin
from .models import Rsvmng


class RsvmngAdmin(admin.ModelAdmin):
    # list_display = ('cstmng', 'goodsmng')        # 어떤 사람이 어떤 상품을 주문했다고 하는 연결 / cstmng PK는 user_sn
    list_display = ('rsv_sn', 'user_sn', 'rsv_dt', 'rsv_time', 'goods_nm', 'ds_class', 'frst_reg_dttm')

admin.site.register(Rsvmng, RsvmngAdmin)

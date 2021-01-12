from django.contrib import admin
from .models import Rsvmng


class RsvmngAdmin(admin.ModelAdmin):
    # list_display = ('hwmsuser', 'goods_nm')
    list_display = ('rsv_sn', 'rsv_dt', 'rsv_time', 'goods_nm', 'ds_class', 'frst_reg_dttm')

    def changelist_view(self, request, extra_context=None):
        extra_context = { 'title': '예약 목록' }
        return super().changelist_view(request, extra_context)

    # yyh : pk 필드 에러 문제 처리 후 풀으면 작동할 것임.
    #
    # def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
    #     rsvmng = Rsvmng.objects.get(pk=object_id)
    #     extra_context = {"title': f"'{rsvmng.cstmng.email}'의 '{rsvmng.goodsmng.goods_nm} ' 예약 수정'"}
    #     return super().changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Rsvmng, RsvmngAdmin)
